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

autocmd TermClose * exe 'bdelete! '..expand('<abuf>') | call DoMappings()
autocmd BufEnter * call DoMappings()

" Terminal that changes to the correct working directory
function Terminal() 
    wincmd j
    if &ft == ''
        call feedkeys("\<C-c>clear\<Enter>")
        return
    endif
    rightbelow sb
    terminal
    call feedkeys("\<C-c>source ~/.bashrc\<Enter>cd ".g:working_dir."\<Enter>clear\<Enter>")
endfunction

" Opens terminal and prepares to compile the current file
function Compile()
    if g:compile_string == ''
        echo 'This filetype is not supported yet'
        return
    endif
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
    return ''
endfunction

" Remaps all keys for the current buffer
function DoMappings()
    silent! unmap <lt>img
    silent! unmap :q<Enter>
    nnoremap <C-r> <nop>
    " Ctrl-r recompiles and runs a file
    nnoremap <silent> <C-r> :Compile<Enter>
    if &ft == ''
        nnoremap <C-c> a<C-c>
        if mode() == 'n'
            call feedkeys("a")
        endif
        return
    endif
    if &ft =~ 'markdown'
        inoremap <img <lt>br><lt>img src="" style="width:auto;display:block;margin:auto"><lt>br> <Esc>?""<Enter>a
        inoremap __ \_\_<lt>ins>()<lt>/ins>\_\_<Esc>/()<Enter>a

        " Markdown-specific behaviour
        nnoremap <silent> <C-r> :MarkdownPreview<cr>
    endif
    if &ft != 'nerdtree'
        let g:compile_string = GetCompileCommand() |
        let g:working_file = expand("%:t")
        let g:working_dir = expand('%:h')
    endif
endfunction

" Convenient mappings
inoremap { {}<left>
inoremap {<Esc> {<Esc>
inoremap {<Enter> {<CR>}<Esc>ko
inoremap $$ $$<left>
nnoremap <silent> <Esc> :noh<cr>
tnoremap <Esc> <C-\><C-n>
tnoremap <C-w> <C-\><C-n><C-w>

nnoremap <silent> <Space><Space> :source ~/.config/nvim/init.vim<cr> | echo 'Reloaded config.'
nnoremap <C-t> :call Terminal()<cr> |
tnoremap <silent> <C-r> <C-\><C-n>:Compile<cr>
