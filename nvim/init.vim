" === init.vim ===
" Loads all required plugins and sources files
" Call nvim with g:training for a training environment
"
" Convenient mappings (Used even in ICPC)
set nocompatible
set showmatch
set hlsearch
set noswapfile
set ignorecase
set autoindent
set tabstop=4
set expandtab
set shiftwidth=4
set softtabstop=4
set relativenumber
set number

inoremap { {}<left>
inoremap {<BS> <nop>
inoremap {} {}
inoremap {<Esc> {<Esc>
inoremap {<Enter> {<CR>}<Esc>ko
nnoremap <silent> <Esc> :noh<cr>

" Subsequent commands are not called during ICPC training
if exists("g:training") | finish | endif

set shell=bash\ -l
set statusline+=%F
set encoding=UTF-8
set autoread
autocmd!

set mouse=a
source ~/.config/nvim/compiler.vim
source ~/.config/nvim/markdown.vim
source ~/.config/nvim/nerdtree.vim
source ~/.config/nvim/keybinds.vim

call plug#begin("~/.vim/plugged")
Plug 'iamcco/markdown-preview.nvim', { 'do': { -> mkdp#util#install() }, 'for': ['markdown', 'vim-plug']}
Plug 'scrooloose/nerdtree'
Plug 'ryanoasis/vim-devicons'
Plug 'folke/tokyonight.nvim', { 'branch': 'main' }
Plug 'mfussenegger/nvim-jdtls'
Plug 'nvim-lualine/lualine.nvim'
Plug 'kyazdani42/nvim-web-devicons'
Plug 'sonph/onehalf', { 'rtp': 'vim' }
Plug 'neovim/nvim-lspconfig'
Plug 'hrsh7th/cmp-nvim-lsp'
Plug 'hrsh7th/cmp-buffer'
Plug 'hrsh7th/cmp-path'
Plug 'hrsh7th/cmp-cmdline'
Plug 'hrsh7th/nvim-cmp'
Plug 'hrsh7th/cmp-vsnip'
Plug 'hrsh7th/vim-vsnip'
call plug#end()

colorscheme onehalfdark

lua <<END
    require('plugins')
    require('lualine').setup()
    require('language')
END
