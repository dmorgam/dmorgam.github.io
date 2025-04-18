#!/bin/sh


BASEDIR=$(dirname "$0")
AWS_BUCKET='public-dmorgam-web'
CLOUDFRONT_DIST='E7J6SXEMEFQ77'

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

serveDev () {
    echo 'Starting dev server...'
    npm run serve
}

buildAws () {
    buildProd
    echo 'Subiendo a AWS...'

    # Delete old objects
    aws s3 rm s3://${AWS_BUCKET}/web/ --recursive

    # Upload new objects
    aws s3 cp ${BASEDIR}/dist/ s3://${AWS_BUCKET}/web/ --recursive --acl public-read

    echo 'Invalidando cache de cloudfront...'
    # Invalidate cloudfront cache
    aws cloudfront create-invalidation --distribution-id ${CLOUDFRONT_DIST} --paths "/*"  --no-cli-pager
}

case $1 in
  '--help')
    showHelp
    ;;
  '--build')
    buildProd
    ;;
  '--serve-dev')
    serveDev
    ;;
  '--build-aws')
    buildAws
    ;;
  *)
    showHelp
    ;;
esac
