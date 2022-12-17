" MarkdownPreview settings
let g:mkdp_auto_start = 0
let g:mkdp_auto_close = 0
let g:mkdp_theme = 'dark'
let g:mkdp_markdown_css = ''

function Print()
    let g:mkdp_theme = 'light'
    let g:mkdp_markdown_css = expand('~/.config/nvim/print.css')
    MarkdownPreview
endfunction
