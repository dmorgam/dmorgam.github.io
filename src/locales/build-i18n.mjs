import fs from "fs"
import path from "path"
import YAML from "yaml"

const srcDir = path.resolve("src/locales")
const outDir = path.resolve("src/locales/generated")

console.log("Procesando yamls a json de i18n ... ")

fs.mkdirSync(outDir, { recursive: true })

for (const file of fs.readdirSync(srcDir)) {
    if (!file.endsWith(".yaml")) continue

    console.log("Parsing " + file)

    const lang = file.replace(".yaml", "")
    const yamlText = fs.readFileSync(path.join(srcDir, file), "utf8")
    const data = YAML.parse(yamlText)

    fs.writeFileSync(
        path.join(outDir, `${lang}.json`),
        JSON.stringify(data, null, 2)
    )
}

