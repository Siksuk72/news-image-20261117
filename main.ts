// news-image-20261117 entrypoint (Node 22, standard library only).
// The front page is drawn by draw.py into entry.png beside this file;
// this program just places that image at /output/entry.png, where the
// grader reads it. Outside the grader, MAKEFUN_OUTPUT_DIR stands in
// for /output, e.g.:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
copyFileSync(new URL("./entry.png", import.meta.url),
             join(outDir, "entry.png"));
