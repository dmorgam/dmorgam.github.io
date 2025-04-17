#!/bin/sh


BASEDIR=$(dirname "$0")

showHelp () {
    echo "Opciones de build:"
    echo "    --help           -  Muestra la ayuda."
    echo "    --build          -  Genera el build con npm."
    echo "    --serve-dev      -  Genera el build con npm y levanta un http."
    echo "    --build-aws      -  Genera el build de pro y lo sube a aws."
}

buildProd () {
    echo 'Building for production...'
    npm run build
    cp dist/index.html dist/404.html
}

case $1 in
  '--help')
    showHelp
    ;;
  '--build')
    buildProd
    ;;
  *)
    showHelp
    ;;
esac
