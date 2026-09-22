# 星环流光 · Orbit Flow Keynote：公开示例提示词

本文件记录两张独立风格示例，不是多页演示文稿。两张示例由内置 Image 2 生成，文案为通用示例；用户提供的图片仅作私有风格参考，不随仓库分发。下次复用只需本文件与[风格规范](../../skills/image2-deck-forge/styles/orbit-flow-keynote.md)。

## 示例规划

| 文件 | 比例 | 页型 | 展示重点 |
|---|---|---|---|
| `assets/previews/orbit-flow-keynote.png` | 16:9 | 核心观点内页 | 横版三模块、留白、星环与结论带 |
| `assets/previews/orbit-flow-keynote-portrait.png` | 3:4 | 四模块信息海报 | 竖版卡片网格、编号、业务图标 |

## Shared Style Lock

将以下锁定规则作为同一套图片的共享提示词；每页只改变内容、页型和对应布局。

### Typography / 字体与语言

默认中文优先。主标题使用现代粗黑无衬线，字面饱满、清晰，不做立体挤压；正文用常规黑体。以正文为 1，主标题约 2.6–3.4，副标题约 1.35–1.6，模块标题约 1.2–1.45，数字约 1.7–2.2。不同页面保持相对层级。

普通内容页标题以黑色为主，最多强调一个短词组，用紫 → 洋红过渡 → 橙渐变。不要整段文字渐变。允许封面采用 4–10 个汉字的书法笔刷主标题；选定这一封面模式后，正文、模块与说明仍然使用黑体，不把书法扩散到内页。

### Palette / 色板与比例

保持白色 `#FFFFFF` / 冷白 `#F7F9FC` 为大面积底色；正文 `#07090D`，次级文字 `#333846`；深蓝区 `#001426`；星环高光由 `#1778BD` 到 `#CBE6FF`；短强调由 `#3E20FF` 经 `#8853F5` 到 `#FF6B19`；卡片细边线 `#EAE2DA`。

典型内容页视觉面积约为白/冷白 70–80%、深蓝 10–18%、紫橙与星环高光 5–10%，黑色文字占其余部分。比例随页型微调，但白底始终占主导。紫橙光带使用约 8–18% 的轻透视觉强度，避免覆盖正文形成彩色脏底。

### Grid / 网格与页面节奏

安全边距约为画布宽度的 5–6%，模块间距稳定。标题、编号、正文和结论共享左对齐基线。先确定标题区、内容区和结论区，再安置装饰。

- 16:9：右上星环的可见直径约为画布宽度的 18–25%，部分裁出画布；标题占左上主阅读区，中部放两至三个信息区，底部总结带高约 15–20%。
- 3:4 / 4:5：上方约三分之一承载标题与留白，中部可用 2×2 模块，底部约 15–20% 收束结论。
- 9:16：增加纵向呼吸感，不靠缩字号容纳更多内容；长议程可用单列编号条目。
- 1:1 封面：围绕短标题与星环构图，省去内容卡片；曲线只引导一次阅读。
- 内容量超出当前比例时拆页，不能把竖版八卡布局压进一张普通横版 PPT。

### Containers / 容器、边线与图标

每套作品选择并保持 `cards`（默认）或 `open-grid` 模式。

`cards`：半透明白色矩形卡片、单层浅暖细线、圆角约为短边的 1.5–2%、极弱灰色阴影；卡片内边距一致。`open-grid`：省去卡片底和阴影，只用浅暖细分隔线建立模块。不要在相邻信息页随机切换两种模式。

总结带使用深蓝底与同族圆角，只放一条主要结论；轨道纹理集中在右半边，文字区域维持近纯深蓝。全画布外沿没有黑框。短渐变分隔线、编号下划线、图标线宽和圆端点形态保持一致；箭头仅用于真实顺序。

### Image / 图像与装饰

蓝色星环是右上角的裁切圆形轨迹：深蓝中心、细密蓝白环线、少量细星点，外缘柔和融入白底。内容页把它限制在标题留白之外；不要生成巨型黑洞、火焰、宇宙战场或满版星空。

一条宽而轻的半透明紫橙丝带由左下向右上自然流动，或在标题与内容间形成轻薄波纹。内页不能同时出现多个高对比漩涡、反复交叉的光带或抢字的镜头光斑。总结带里的星轨只是同一母题的低亮度回声。

默认以细线业务图标支持模块含义，不引入机器人、机械手、科幻人物、产品摄影或其它风格的材质。需要数据时用来源中的真实数值，星环不承担数据编码。

### Header and footer / 页眉与页脚

页眉可保留一个简短内容分类，如“AI 工作方法”，配短渐变线；它不是重复品牌标志。总结带只在内容需要明确结论、交付或下一步时出现，不强行添加营销口号。

默认不生成品牌标志、固定字标、水印、二维码、课程名称、日期、地点或联系方式。用户明确需要时使用其确认的信息；标志和可扫描二维码应由用户提供固定资产，预留位置后再放置，不让 Image 2 猜画。公开样例使用虚构、通用文案。

### Text density / 文字密度

普通 16:9 内页：一个短标题、至多一句副标题、两至三个信息点，每点一个短模块名和至多一行解释；一条简短总结。参考中的四卡和八卡海报不自动变成 PPT 默认密度。

明确的竖版信息海报可采用四模块，每模块一个短标题、至多两行解释。只有用户要求阅读型长图时才使用五至八条内容，并优先拆为两张；不为保留卡片数量牺牲可读字号。

### Negative constraints / 风格隔离

不要黑色终端、HUD、代码雨、满版深色背景、霓虹赛博朋克、厚玻璃拟态、重阴影、金属 3D 字、金色奢华材质、无关摄影、每页笔刷字、整段渐变文字、密集段落、假数据、外框、品牌复制或虚构二维码。不要把以前任务中的风格带入本套作品。

## Landscape prompt

将完整 Shared Style Lock 放在以下提示词之前。

```text
Use case: productivity-visual.
Asset type: one finished 16:9 landscape slide for the open-source Orbit Flow Keynote style library.
Input images: the two supplied portrait images are STYLE REFERENCES ONLY. Reinterpret their white canvas, cropped orbital vortex, translucent violet-orange ribbon, typographic hierarchy and navy conclusion band for a sparse landscape slide. Do not copy any source names, identity marks, dates, QR codes, event details, or wording.
Page role: inner slide / core claim. Component mode: cards. Information-first, quiet background, restrained ornaments, readable text hierarchy.
Layout: 5–6% safe margins, bold Chinese headline in the upper left; cropped blue orbit in the upper right only, no more than one quarter of the canvas width; one softly translucent violet-orange ribbon behind whitespace. Three equally sized white rounded cards across the middle, fine warm-gray outlines, subtle shadows, one small consistent line icon per card, large numbers with short purple-orange underline. A wide inset navy band across the bottom contains one short conclusion; faint orbital lines on its right, clear navy behind the text. White must dominate.
Visible text, verbatim and nothing else:
Top label: “AI 工作方法”
Main title: “让 AI 进入真实工作”
Subtitle: “把知识连接成可持续的方法”
Card 1: “01” / “理解问题” / “从具体任务开始”
Card 2: “02” / “连接知识” / “让经验可以复用”
Card 3: “03” / “形成行动” / “把方法落到流程”
Conclusion: “让每一步，都成为下一步的基础”
Main headline black, with only “真实工作” in a violet-to-orange gradient. Crisp readable Chinese characters. No brush lettering on this inner slide, no logos, no watermarks, no outer perimeter border, no QR code, no calendar or event details. Produce one single full slide, not a collage.
```

## Portrait prompt

将完整 Shared Style Lock 放在以下提示词之前。

```text
Use case: productivity-visual.
Asset type: one finished 3:4 portrait information poster for the open-source Orbit Flow Keynote style library.
Input images: the two supplied portrait images are STYLE REFERENCES ONLY. Follow their light business-tech visual DNA, not their text, logos, dates, locations, or QR codes.
Page role: portrait framework. Component mode: cards. Preserve the same restrained white, black, blue-orbit, violet-orange visual language as the landscape example.
Layout: a broad white title zone with a blue orbital vortex cropped off the top-right corner; a single soft translucent lavender-to-orange ribbon flowing behind whitespace; a spacious 2x2 grid of white translucent cards with equal warm-gray thin borders and consistent soft rounded corners. Each card has a bold number, short violet-orange underline, black module title, one short black line of description and a small consistent outline icon. One inset deep-navy rounded conclusion band at the bottom, orbital texture only on the right. White background remains dominant. Keep 5–6% safe margins and large readable Chinese type.
Visible text, verbatim and nothing else:
Top label: “AI 能力框架”
Main title: “把能力，变成系统”
Subtitle: “从一次尝试，到持续复用”
Card 1: “01” / “系统思维” / “先看关系，再选工具”
Card 2: “02” / “知识沉淀” / “让经验成为长期资产”
Card 3: “03” / “流程协同” / “让任务自然衔接”
Card 4: “04” / “持续迭代” / “让反馈推动下一步”
Conclusion: “让经验留下，让方法复用”
Only “系统” in the main headline may use a violet-to-orange gradient. No source identity, no brands, no date or venue, no QR codes, no logos, no outer black frame, no dark full-bleed background, no brush text, no heavy glass UI, no photographic subjects. One finished portrait image, no collage.
```

## Repository atlas prompt

风格总览是独立的目录展示图；输入为仓库的初版五风格总览与新的星环流光横版示例，共两张参考图。

```text
Use case: productivity-visual.
Asset type: 16:9 GitHub repository hero, a visual style atlas comparing six styles.
Input image 1: the existing five-style atlas, providing Terminal Tech, Impact Grid, Climate Impact, French Commerce, and Aubergine Future. Input image 2: the new Orbit Flow landscape preview. These are STYLE REFERENCES ONLY. Each panel must keep only the visual language of its corresponding reference.
Create a premium contact sheet on a neutral charcoal field. Six equal landscape 16:9 miniature slide panels in an exact 3-column by 2-row grid, generous small gutters, no tilted cards or perspective. Place one clear header across the top: "SIX VISUAL SYSTEMS. ONE DECK FORGE."
Under each panel place its exact label in white:
top-left "TERMINAL TECH"
top-middle "IMPACT GRID"
top-right "CLIMATE IMPACT"
bottom-left "FRENCH COMMERCE"
bottom-middle "AUBERGINE FUTURE"
bottom-right "ORBIT FLOW"
For each panel retain the reference's strongest recognisable composition and image:
1 black terminal, mint signals;
2 warm-white editorial grid, documentary institution, dark teal;
3 white editorial grid, muted coastal wind turbines;
4 cream and caramel fashion still life with burgundy handbag;
5 aubergine architectural passage and ivory type;
6 white business-tech layout, cropped blue orbit at upper right, translucent purple-orange wave, black Chinese type, three numbered light cards, navy conclusion band.
Keep each miniature restrained and readable as a style sample. Do not force the violet-orange colors into any other panel. This is a comparison atlas, not a single slide or deck. No corporate logos, event data, QR codes, device mockups, people holding pages, dates, watermarks, or outer rectangular frame. Simplify tiny source text if needed; prioritize faithful visual identity over adding unreadable microtext.
```
