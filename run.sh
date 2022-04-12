#!env sh



if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    echo ""
    echo "USAGE: ./run.sh COMMAND"
    echo ""
    echo "COMMANDS:"
    echo "  check: check python code for errors using pyright"
    exit 1
fi

if [ "$1" == "check" ]; then
    poetry run pyright
fi
if [ "$1" == "format" ]; then
    poetry run black src
fi
if [ "$1" == "test" ]; then
    poetry run pytest tests
fi