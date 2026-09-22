# Image 2 Deck Forge｜视觉演示锻造炉

> **把文档锻造成一套有灵魂、有秩序、有电影感的视觉演示。**  
> Turn raw documents into cinematic, image-first presentations with a locked visual language.

![六套内置视觉系统 / Six built-in visual systems](https://raw.githubusercontent.com/lp7743951-star/image2-deck-forge/main/assets/style-atlas-six.png)

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111111)](skills/image2-deck-forge/SKILL.md)
[![Visual Systems](https://img.shields.io/badge/Visual%20Systems-6-5f2d66)](skills/image2-deck-forge/styles/catalog.md)
[![Renderer](https://img.shields.io/badge/Renderer-Image%202-20c997)](#工作方式--how-it-works)
[![License](https://img.shields.io/badge/License-MIT-f4c95d)](LICENSE)

**Image 2 Deck Forge** 是一个面向 Codex 的图片型 PPT Skill。它会从文章、方案、网页或原始文档中提炼叙事，锁定一套视觉系统，为每页规划清晰的视觉命题，再使用 Image 2 生成完整的 16:9 幻灯片图片，最终组装为 image-only PPTX。

Image 2 Deck Forge is a reusable Codex skill that extracts the argument, locks one visual system, plans each slide, renders it with Image 2, and packages the approved images into an image-only deck.

**不是随机套模板，不是十二张互不认识的 AI 图片，也不是披着设计外衣的信息堆积。**  
No theme roulette. No identity drift. No decorative AI wallpaper pretending to be visual reasoning.

## 六套视觉系统｜Six Visual Systems

| 视觉系统 | 中文定位 | Best for |
|---|---|---|
| Terminal Tech Magazine | 冷静、精密的终端科技杂志 | AI, devtools, systems, security |
| Impact Grid Editorial | 具有公共表达力量的机构编辑设计 | Strategy, research, consulting |
| Climate Impact Editorial Grid | 环境证据与瑞士网格的结合 | Climate, ESG, sustainability |
| French Editorial Commerce | 法式商业杂志与高质感产品叙事 | Fashion, retail, beauty, lifestyle |
| Aubergine Semantic Future | 拒绝机器人套图的语义未来主义 | AI futures, transformation, concepts |
| Orbit Flow Keynote | 白底星环、紫橙流光与清晰商务表达 | AI workshops, product keynotes, business posters |

### 01 · Terminal Tech Magazine｜终端科技杂志

![Terminal Tech Magazine](https://raw.githubusercontent.com/lp7743951-star/image2-deck-forge/main/assets/previews/terminal-tech-magazine.png)

黑色终端表面、薄荷与青色信号、克制的系统几何。技术感来自结构与信息，而不是赛博朋克噪声。

Near-black terminal surfaces, mint/cyan signals, credible technical imagery, and exactly zero cyberpunk clutter.

### 02 · Impact Grid Editorial｜影响力网格编辑

![Impact Grid Editorial](https://raw.githubusercontent.com/lp7743951-star/image2-deck-forge/main/assets/previews/impact-grid-editorial.png)

暖白纸张、硬朗网格、深青色模块与纪实影像。让战略、研究和机构观点在缩略图尺寸下依然有力量。

Warm paper, hard editorial modules, documentary evidence, and an argument that reads from the back row.

### 03 · Climate Impact Editorial Grid｜气候影响力编辑网格

![Climate Impact Editorial Grid](https://raw.githubusercontent.com/lp7743951-star/image2-deck-forge/main/assets/previews/climate-impact-editorial-grid.png)

冷白纸张、低饱和环境摄影、海玻璃青与证据优先的叙事。拒绝叶子图标、发光地球和廉价绿色包装。

Cool paper, muted field photography, sea-glass accents, and an evidence-first environmental voice.

### 04 · French Editorial Commerce｜法式商业编辑

![French Editorial Commerce](https://raw.githubusercontent.com/lp7743951-star/image2-deck-forge/main/assets/previews/french-editorial-commerce.png)

奶油纸张、窄体标题、衬线字对比与触感影像。商业表达可以有欲望、有品位，但不必落入“奢华金色”俗套。

Cream paper, condensed display type, serif contrast, tactile imagery, and taste without the luxury cliché machine.

### 05 · Aubergine Semantic Future｜紫茄语义未来

![Aubergine Semantic Future](https://raw.githubusercontent.com/lp7743951-star/image2-deck-forge/main/assets/previews/aubergine-semantic-future.png)

深紫茄色、象牙白与淡金、纪念碑式大字，以及真正从页面命题中选择的语义图像。机器人和机械手默认限量使用。

Deep plum, ivory and pale gold, monumental type, and imagery chosen from the meaning of the claim. Robots are rationed.

### 06 · Orbit Flow Keynote｜星环流光 · NEW

![星环流光横版示例 / Orbit Flow landscape preview](https://raw.githubusercontent.com/lp7743951-star/image2-deck-forge/main/assets/previews/orbit-flow-keynote.png)

白底、右上角裁切蓝色星环、半透明紫橙丝带、粗黑中文标题与深蓝总结区，形成清晰的商务科技表达。封面可用短书法标题；内页采用统一编号模块、细线图标和轻透卡片。

A white business-tech system with a cropped blue orbital vortex, translucent violet-orange flow, bold Chinese typography, numbered modules, and a navy conclusion band. Short brush lettering is reserved for covers.

支持 16:9 PPT 与 3:4 / 4:5 / 9:16 竖版信息海报：横版控制在两至三个信息点，竖版可以使用四模块。适合 AI 工作坊、产品发布、能力框架和活动介绍。

Layouts adapt to landscape decks and portrait posters instead of squeezing one format into another. The public examples contain no source logos, event dates, locations, or QR codes.

<details>
<summary>展开查看 3:4 竖版示例 / Portrait preview</summary>

<img src="https://raw.githubusercontent.com/lp7743951-star/image2-deck-forge/main/assets/previews/orbit-flow-keynote-portrait.png" alt="星环流光竖版四模块示例" width="480">

</details>

[阅读完整风格规范 / Style contract](skills/image2-deck-forge/styles/orbit-flow-keynote.md) · [示例提示词 / Example prompts](examples/orbit-flow-keynote/prompts.md)

## 它为什么不同｜Why It Is Different

- **一份 Deck 只锁定一套 Style Lock。** 字体、色板、网格、容器、图片方向、文字密度与禁用项全程一致。  
  **One Style Lock per deck.** Typography, palette, grid, containers, density, imagery, and negative rules remain coherent.
- **语义先于图片。** 每一张视觉都必须推进页面命题，而不是只负责“看起来未来”。  
  **Meaning before imagery.** Every visual must advance the slide thesis.
- **真正有用的审核节点。** 先看大纲与 prompts，再看缩略图板，最后生成完整页面。  
  **Approval gates that matter.** Outline, prompt plan, thumbnail board, then full-size slides.
- **图片即最终幻灯片。** PPTX 是对已批准 16:9 图片的忠实封装。  
  **Image-only output.** The final PPTX preserves approved slide images exactly.
- **可扩展风格库。** 新增风格不是换色，而是新增一份完整的视觉行为合同。  
  **Built to extend.** Add a complete visual contract, not a palette swap.
- **单页返修不漂移。** 修改目标页，同时保护整套演示的视觉 DNA。  
  **Revision without identity drift.** Repair one slide without breaking the deck.

## 工作方式｜How It Works

```text
原始文档 / source document
    -> 叙事提炼 / narrative extraction
    -> 风格选择 / style selection
    -> 页面架构 / slide architecture
    -> Image 2 prompts
    -> 缩略图板 / thumbnail board
    -> 独立 16:9 页面 / approved slide renders
    -> image-only PPTX + source images
```

所有视觉页面均由 Image 2 生成。该 Skill 不会用 HTML、SVG、Canvas 或程序化绘图重建幻灯片。

Every visual slide is rendered with Image 2. The skill does not reconstruct visual pages with HTML, SVG, canvas, or programmatic drawing.

## 安装｜Install

```bash
git clone https://github.com/lp7743951-star/image2-deck-forge.git
cp -R image2-deck-forge/skills/image2-deck-forge ~/.codex/skills/
```

调用示例 / Example prompts:

```text
使用 $image2-deck-forge，把这份战略文档做成 12 页图片型 PPT。
使用 Aubergine Semantic Future 风格，先给我看缩略图板。

Use $image2-deck-forge to turn this strategy document into a 12-slide deck.
Use Aubergine Semantic Future and show me the thumbnail board first.
```

调用新风格 / Try the new style:

```text
使用 $image2-deck-forge，调用“星环流光”（orbit-flow-keynote），
把这份材料做成 8 页 16:9 图片型 PPT，先输出大纲和 prompts。

使用 $image2-deck-forge，调用 Orbit Flow Keynote，
生成一张 3:4 四模块业务介绍海报，不含品牌、日期或二维码。
```

风格别名 / Aliases: `Orbit Flow`、`星环流光`、`白底星环`、`紫橙流光`。

## 创建自己的风格｜Create Your Own Style

1. 复制 [`styles/`](skills/image2-deck-forge/styles/) 中的一份风格文件。
2. 定义 Identity、Use、Visual DNA、Style Lock、Page Behavior、Prompt Prefix 与 Quality Gate。
3. 将新风格加入 [风格目录](skills/image2-deck-forge/styles/catalog.md)。
4. 运行校验：

```bash
python skills/image2-deck-forge/scripts/validate_style_library.py
```

完整规范见 [Style Authoring](skills/image2-deck-forge/references/style-authoring.md)。

## 仓库结构｜Repository Map

```text
skills/image2-deck-forge/
|-- SKILL.md
|-- agents/openai.yaml
|-- styles/                 # 六套可复用视觉系统
|-- references/             # 工作流、页面类型、交付与返修规范
`-- scripts/validate_style_library.py

assets/
|-- style-atlas-six.png      # 六风格总览
|-- style-atlas.png          # 初版五风格总览，保留旧链接
`-- previews/               # 风格效果图，含星环流光横版与竖版

examples/orbit-flow-keynote/
`-- prompts.md              # 新风格示例的共享规则与出图提示词
```

## 设计承诺｜Design Promise

一套演示不应该像十二条互不相关的提示词碰巧共享了同一个文件名。Image 2 Deck Forge 把 PPT 当作一个完整的视觉世界：有叙事推进、有重复的构图逻辑，也有受控的变化。

A deck should not look like twelve unrelated prompts that accidentally share a filename. Image 2 Deck Forge treats a presentation as one visual world with narrative progression, recurring composition logic, and controlled variation.

仓库中的参考图均为展示内置视觉系统而专门生成，不包含第三方模板或品牌资产。

## License

MIT。欢迎 Fork、扩展风格库，并把下一份演示做得让人无法忽视。  
MIT. Fork it, extend it, and make the next deck impossible to ignore.

