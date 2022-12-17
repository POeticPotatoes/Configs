nnoremap <silent> <Space><Space> :source ~/.config/nvim/init.vim<cr> | echo 'Reloaded config.'

inoremap } <Esc>:call SkipBrace('}')<cr>a}
inoremap ) <Esc>:call SkipBrace(')')<cr>a)
inoremap ] <Esc>:call SkipBrace(']')<cr>a]
inoremap $ <Esc>:call SkipBrace('$')<cr>$]

inoremap ( ()<left>
inoremap [ []<left>
inoremap $$ $$<left>
tnoremap <Esc> <C-\><C-n>
tnoremap <C-w> <C-\><C-n><C-w>

function SkipBrace(e)
    let lastchar = getline('.')[col('.')]
    echomsg "last item: ". lastchar
    if lastchar==#a:e
        call feedkeys("\<Esc>xa")
    endif
endfunction
