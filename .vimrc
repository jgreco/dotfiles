"- AESTHETIC -"

set encoding=utf-8
syntax enable
set relativenumber number

set bg=dark

" Different cursor shapes in different modes
let &t_SI = "\<Esc>[4 q"
let &t_SR = "\<Esc>[4 q"
let &t_EI = "\<Esc>[2 q"


"- BASIC FUNCTIONALITY -"

inoremap jj <Esc>
let mapleader = ","

tnoremap <Esc> <C-\><C-n>

set spelllang=en
nnoremap s :setlocal spell!<cr>

nnoremap <leader>w :call system('wl-copy', @")<cr>

nnoremap q: <nop>
nnoremap Q  <nop>


"- INDENTATION -"

filetype plugin indent on
set autoindent


"- COMMENTS -"

nnoremap #  I#<Esc>
nnoremap // I//<Esc>
nnoremap -- I--<Esc>
nnoremap /* I/* <Esc>A */<Esc>
vnoremap /* c/**/<Left><Left><Esc>p

nnoremap ;; A;<Esc>


"- SEARCH -"

set ignorecase smartcase
set incsearch
set grepprg=rg\ --vimgrep


"- AUTOCLOSE -"

vnoremap <leader>{ c{}<Left><Esc>p
vnoremap <leader>( c()<Left><Esc>p
vnoremap <leader>" c""<Left><Esc>p
vnoremap <leader>[ c[]<Left><Esc>p
vnoremap <leader>' c''<Left><Esc>p
vnoremap <leader>< c<><Left><Esc>p


"- READLINE -"
" This isn't even close to complete but it's all that matters to me. C-p and
" C-n are omitted since they have special meanings already.

inoremap <C-a> <Home>
inoremap <C-e> <End>
inoremap <C-d> <Delete>
inoremap <C-k> <Esc>c$
inoremap <C-f> <Right>
inoremap <C-b> <Left>


"- WINDOWS -"

nnoremap H <C-w>h
nnoremap J <C-w>j
nnoremap K <C-w>k
nnoremap L <C-w>l


"- ALE -"

let g:ale_lint_on_text_changed = "never"
let g:ale_c_gcc_options = '-std=c90 -Wall'
let g:ale_lint_on_insert_leave = "0"


"- MISCELLANEOUS -"

nnoremap <leader>e :vsplit $MYVIMRC<cr>
nnoremap <leader>s :source $MYVIMRC<cr>

packloadall
silent! helptags ALL
