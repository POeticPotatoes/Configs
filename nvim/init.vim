set showmatch
set autoread
set ignorecase
set hlsearch
set wildmode=longest, list
set mouse=a
set encoding=UTF-8
set noswapfile
set autoindent
set tabstop=4
set expandtab
set shiftwidth=4
set softtabstop=4
set statusline+=%F
set relativenumber
set shell=bash\ -l
set number

colorscheme  onehalfdark

" MarkdownPreview settings
let g:mkdp_auto_start = 0
let g:mkdp_auto_close = 0
let g:mkdp_theme = 'dark'

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


" Notification after file change
autocmd FocusGained,BufEnter,CursorHold,CursorHoldI * if mode() != 'c' | checktime | endif
\ echohl WarningMsg | echo "File changed on disk. Buffer reloaded." | echohl None

lua <<END
  require('plugins')
  require('lualine').setup()
END

" Convenient mappings
inoremap { {}<left>
inoremap {<Esc> {<Esc>
inoremap {<Enter> {<CR>}<Esc>ko
inoremap $$ $$<left>
nnoremap <silent> <Esc> :noh<cr>
nnoremap <silent> <Space><Space> :source ~/.config/nvim/init.vim<cr> | echo 'Reloaded config.'
nnoremap <C-t> :call Terminal()<cr> |
tnoremap <Esc> <C-\><C-n>
tnoremap <C-w> <C-\><C-n><C-w>

" Commands for specific actions
command Mdp MarkdownPreview
command Terminal call Terminal()
command Compile call Compile()
command ReloadMappings call DoMappings()

autocmd FileType markdown 
autocmd BufEnter * call DoMappings()
autocmd TermClose * if !v:event.status | exe 'bdelete! '..expand('<abuf>') | endif

" Terminal that changes to the correct working directory
function Terminal() 
    let g:working_dir = expand('%:h')
    rightbelow sb
    terminal
    call feedkeys("acd ".g:working_dir."\<Enter>clear\<Enter>")
endfunction

" Opens terminal and prepares to compile the current file
function Compile()
    let g:working_file = expand("%:t")
    call Terminal()
    call feedkeys("compile -a ".g:working_file)
endfunction

" Remaps all keys for the current buffer
function DoMappings()
    silent! unmap <lt>img
    silent! unmap :q<Enter>
    silent! unmap <C-c>
    if &ft =~ 'markdown'
        inoremap <img <lt>br><lt>img src="" style="width:auto;display:block;margin:auto"><lt>br> <Esc>?""<Enter>a
        inoremap __ \_\_<lt>ins>()<lt>/ins>\_\_<Esc>/()<Enter>a
    endif
    if &ft =~ 'cpp'
        nnoremap <C-c> :call Compile()<cr>
    endif
    if &ft == ''
        nnoremap :q<Enter>aclear<Enter>exit<Enter>
    endif
endfunction
