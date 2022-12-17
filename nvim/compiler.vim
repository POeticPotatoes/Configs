nnoremap <silent> <Space><Space> :source ~/.config/nvim/init.vim<cr> | echo 'Reloaded config.'
nnoremap <silent> <C-t> :call Terminal()<cr>
nnoremap <silent> <C-p> :call CreateTest()<cr>

command Terminal call Terminal()
command Compile call Compile()
command ReloadMappings call DoMappings()

autocmd TermClose * q | call DoMappings()
autocmd BufEnter * call DoMappings()

" =============================================
let g:compile_string = 'cat '

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
        return 'python3 '
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
