# 关键验收报告 — xinqiutent.com (?v=v1)
只读验收，未修改站点任何文件。Chrome 自动翻译已通过 `translate="no"` + `<meta name="google" content="notranslate">` 抑制（每页注入后确认 `translated-ltr` = false，页面保持英文原文）。

## 视口
- 首页/图标检查：1440 × 900（部分区域用 1440 × 1700 单屏覆盖）
- 产品网格：1440 × 900（按要求）
- 滚动：临时将 `scroll-behavior` 覆盖为 `auto`（页面默认 smooth，导致瞬时读取 scrollY 恒为 0），未改动页面源文件

## 一、图标渲染 —— 通过
站点图标字体为**子集字体**（需逐字形核验）：
- `Font Awesome 6 Free` → `/assets/css/fa/fa-solid-900.subset.woff2`（status: loaded）
- `Font Awesome 6 Brands` → `/assets/css/fa/fa-brands-400.subset.woff2`（status: loaded）
（另有 cdnjs font-awesome 6.0.0 all.min.css，是否被覆盖需注意；实测生效的是本地子集）

视觉确认正常渲染（无空白/方块/问号）：
- 特性区：fa-industry / fa-shield-alt / fa-leaf / fa-globe-americas
- FAQ：fa-chevron-down × 20 全部为橙色箭头
- 页脚社媒：fa-linkedin / fa-instagram / fa-tiktok / fa-facebook（+ far fa-id-card）全部为品牌图形
- 联系区：fa-paper-plane、fab fa-whatsapp
- 合规图标：fa-flask(ISO 811/13937)、fa-fire-extinguisher(CPAI-84)、fa-shield-virus(EN71)、fa-certificate、fa-award、fa-clipboard-check、fa-industry、fa-shield-alt
- 其他：fa-file-download、fa-arrow-right（View Details）、fab fa-whatsapp / fa-file-pdf（右下浮动按钮）
- "实力数据带"（Est. 2006 / BSCI Audited / 3,300㎡ / ~70%）本身为纯文字胶囊，**该区域没有图标**
- fa-play（YouTube 播放）：实测 24×18px，未单独截图视觉确认（非本次关注项）

## 二、产品网格 —— 基本通过（1 项残留）
"Global Export Selection - 2026 Camping Tents"（11 张卡片，grid lg:grid-cols-4 gap-8）
- 图片留白：图片框 238.9px 高，图片渲染 222.9px，上下 padding 各 8px → 每侧由修复前 ~24.5px 降到 8px。**已修复**（占框 93.3%）
- 图片本身：11/11 全部加载成功（complete=true，natural 480–640px 正方形）；`object-fit: contain` → 无裁剪、无变形、未溢出卡片
- 卡片高度/CTA：同行卡片等高，`Factory Direct` + `Request Quote` 行 y 完全对齐（第1行 1172.1 / 第2行 1708.1 / 第3行 2216.1），**未再被推下**
- 标题：标题**顶部**对齐（同行 titleTop 相同），但**行数仍不一致**：第1行 3/3/3/4、第2行 4/3/3/3、第3行 3/3/3。第4张卡文案较长自然折 4 行 → 残留问题
- 新问题：无布局类新问题。仅第2行第1张卡多一行价格（US$100.00 | MOQ: 1 pc），属内容差异

## 三、主题 —— 通过
4 个页面 body 背景均为 `rgb(11,15,23)` (#0B0F17) + 橙色 (#F59E0B/#FB923C) 点缀：
- news.html（Technical Intelligence Library）：通过（内容面板 #131926）
- news/1-factory-capacity-expansion-for-2026-peak-season.html：通过
- about.html（The Soul of Xinqiu）：通过
- privacy.html：通过
无白底 / 浅灰底 / 蓝色系残留。

## 附加观察（超出三项范围，供参考）
- camping-tents.html 的 `<nav>` 为 `position:fixed` 且 `top:80px`，滚动时顶部会露出约 80px 页面内容（该页截图可见卡片残影）。索引页 / 隐私页实测 nav 在 top:0，故推测该页顶部有公告条占位。低风险，未深查。
- 首页分类卡 / 新闻卡的图片为懒加载，刚进入视口时短暂显示灰色空框；停留后正常加载。

## 截图
见本报告末尾消息中的 CDN 链接（同时保存在 ./qa/）。
