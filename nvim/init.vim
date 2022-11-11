set nocompatible
set showmatch
set autoread
set hlsearch
set wildmode=longest, list
set mouse=a
set encoding=UTF-8
set noswapfile
set ignorecase
set autoindent
set tabstop=4
set expandtab
set shiftwidth=4
set softtabstop=4
set statusline+=%F
set relativenumber
set shell=bash\ -l
set number
autocmd!

" MarkdownPreview settings
let g:mkdp_auto_start = 0
let g:mkdp_auto_close = 0
let g:mkdp_theme = 'dark'

" Custom terminal management
let g:compile_string = 'cat '

" NERDTree settings
let NERDTreeShowLineNumbers=1
autocmd VimEnter * if !filereadable(@%) | if argc() == 1 && isdirectory(argv()[0]) |
            \ execute 'edit  ' . argv()[0] . '/README.md' | execute 'NERDTree' argv()[0] |  else | NERDTree | endif | wincmd p | endif
autocmd BufEnter * if winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif
autocmd BufWinEnter * if getcmdwintype() == '' | silent NERDTreeMirror | endif
autocmd FileType nerdtree setlocal relativenumber

inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ CheckBackspace() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! CheckBackspace() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" Plugged programs
call plug#begin("~/.vim/plugged")
Plug 'iamcco/markdown-preview.nvim', { 'do': { -> mkdp#util#install() }, 'for': ['markdown', 'vim-plug']}
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'scrooloose/nerdtree'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'ryanoasis/vim-devicons'
Plug 'folke/tokyonight.nvim', { 'branch': 'main' }
Plug 'mfussenegger/nvim-jdtls'
Plug 'nvim-lualine/lualine.nvim'
Plug 'kyazdani42/nvim-web-devicons'
Plug 'sonph/onehalf', { 'rtp': 'vim' }
call plug#end()

colorscheme  onehalfdark

" trigger `autoread` when files changes on disk
autocmd FocusGained,BufEnter,CursorHold,CursorHoldI * if mode() != 'c' | checktime | endif
" notification after file change
autocmd FileChangedShellPost *
  \ echohl WarningMsg | echo "File changed on disk. Buffer reloaded." | echohl None

lua <<END
  require('plugins')
  require('lualine').setup()
END

" Commands for specific actions
command Terminal call Terminal()
command Compile call Compile()
command ReloadMappings call DoMappings()

autocmd TermClose * q | call DoMappings()
autocmd BufEnter * call DoMappings()

" Terminal that changes to the correct working directory
function Terminal() 
    wincmd j
    if &buftype == 'terminal'
        startinsert
        call feedkeys("\<C-c>\<Enter>clear\<Enter>")
        return
    endif
    rightbelow sb
    terminal
    startinsert
    sleep 100m
    call feedkeys("source ~/.bashrc\<Enter>cd ".g:working_dir."\<Enter>clear\<Enter>")
endfunction

" Opens terminal and prepares to compile the current file
function Compile()
    if g:compile_string == ''
        echo 'This filetype is not supported yet'
        return
    endif
    w
    Terminal
    call feedkeys(g:compile_string.g:working_file."\<Enter>")
endfunction

" Returns the compile string for a filetype.
" Uses my custom .bashrc commands
function GetCompileCommand()
    if &ft == ''
        return g:compile_string
    endif
    if &ft =~ 'cpp'
        return 'runcpp '
    endif
    if &ft =~ 'python'
        return 'python '
    endif
    if &ft =~ 'c'
        return 'runc '
    endif
    if &ft =~ 'java'
        return 'java '
    endif
    if &ft =~ 'input'
        return 'test '
    endif
    return ''
endfunction

" Remaps all keys for the current buffer
function DoMappings()
    silent! unmap <lt>img
    silent! unmap :q<Enter>
    " Ctrl-c recompiles and runs a file
    nnoremap <silent> <C-g> :Compile<cr>
    if &buftype =~ 'terminal'
        nnoremap <C-c> a<C-c>
        startinsert
        return
    endif
    if &ft =~ 'markdown'
        inoremap <img <lt>br><lt>img src="" style="width:auto;display:block;margin:auto"><lt>br> <Esc>?""<Enter>a
        inoremap __ \_\_<lt>ins>()<lt>/ins>\_\_<Esc>/()<Enter>a

        " Markdown-specific behaviour
        nnoremap <silent> <C-g> :MarkdownPreview<cr>
    endif
    if &ft != ''
        let g:compile_string = GetCompileCommand() |
        let g:working_file = expand("%:t")
        let g:working_dir = expand('%:h')
    endif
endfunction

function CreateTest()
    tabnew
    execute "cd" g:working_dir
    execute "edit" g:working_file[:-5].".in"
endfunction

" Convenient mappings
inoremap { {}<left>
inoremap {<BS> <nop>
inoremap {} {}
inoremap {<Esc> {<Esc>
inoremap {<Enter> {<CR>}<Esc>ko
inoremap $$ $$<left>
nnoremap <silent> <Esc> :noh<cr>
tnoremap <Esc> <C-\><C-n>
tnoremap <C-w> <C-\><C-n><C-w>

nnoremap <silent> <Space><Space> :source ~/.config/nvim/init.vim<cr> | echo 'Reloaded config.'
nnoremap <silent> <C-t> :call Terminal()<cr>
nnoremap <silent> <C-p> :call CreateTest()<cr>

au BufNewFile,BufRead *.in set filetype=input
au BufNewFile,BufRead *bash set filetype=terminal
