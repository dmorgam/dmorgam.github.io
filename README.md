# dmorgam.github.io

New deployment location: https://***dmorgam.com
Serverless setup in aws

## Project setup

```
npm install
```

### Yamls con locales transformados a json

Script build-i18n.mjs que transfoma los yaml a json para los locales.

```json
  "scripts": {
    "i18n:build": "node src/locales/build-i18n.mjs",
    "serve": "npm run i18n:build && vue-cli-service serve",
    "build": "npm run i18n:build && vue-cli-service build",
    "lint": "vue-cli-service lint"
  },
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
