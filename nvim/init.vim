set nocompatible
set showmatch
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
set number
let g:mkdp_auto_start = 0
let g:mkdp_auto_close = 0
let g:mkdp_theme = 'dark'
let NERDTreeShowLineNumbers=1

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

" Use <c-space> to trigger completion.
" if has('nvim')
"   inoremap <silent><expr> <c-space> coc#refresh()
" else
"   inoremap <silent><expr> <c-@> coc#refresh()
" endif

set autoread
autocmd FocusGained,BufEnter,CursorHold,CursorHoldI * if mode() != 'c' | checktime | endif
" notification after file change
\ echohl WarningMsg | echo "File changed on disk. Buffer reloaded." | echohl None

lua <<END
  require('plugins')
  require('lualine').setup()
END

" Convenient mappings
" autocmd BufEnter * if &ft =~ 'cpp\|c\|java' | 
"             \ inoremap { {<CR>}<Esc>ko |
"             \ else | inoremap { {}<left> | endif
autocmd BufEnter * if &ft =~ 'markdown' | 
            \ inoremap __ \_\_<lt>ins>()<lt>/ins>\_\_<Esc>/()<Enter>a |
            \ else | inoremap __ | endif | echo 'Underlined'
inoremap { {}<left>
inoremap {<Esc> {<Esc>
inoremap {<Enter> {<CR>}<Esc>ko
inoremap $$ $$<left>
nnoremap <silent> <Enter> :MarkdownPreview<cr>
nnoremap <silent> <Esc> :noh<cr>
nnoremap <silent> <Space><Space> :source ~/.config/nvim/init.vim<cr> | echo 'Reloaded config.'
autocmd FileType markdown inoremap <img <lt>br><lt>img src="" style="width:auto;display:block;margin:auto"><lt>br> <Esc>?""<Enter>a

