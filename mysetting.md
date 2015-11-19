# My Setting for file_neglected_checker

The file_neglected_checker is designed to run under Python 3.4.3.

On my Mac OS X, Python 3.4.3 was installed as following:

- Install pyenv

  `brew install pyenv`

  *Note* : Don't forget to add `if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi` to .zshrc

- Install readline

  `brew install readline`

- Install Python 3.4.3

  `CFLAGS="-I$(brew --prefix openssl)/include" \                        [~]
  LDFLAGS="-L$(brew --prefix openssl)/lib" \
  pyenv install -v 3.4.3`

- To use Python 3.4.3, run `pyenv local 3.4.3` in file_neglected_checker folder
