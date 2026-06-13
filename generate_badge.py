from datetime import datetime
from zoneinfo import ZoneInfo

# ========== 你只需要改这里就行 ==========
# 上次更新日期，格式：年-月-日（北京时间）
LAST_UPDATE_DATE = "2026-06-13"
# 徽章显示的文字前缀
LABEL_TEXT = "距离上次更新"
# 徽章后缀
SUFFIX_TEXT = "天"
# 徽章尺寸与样式
BADGE_WIDTH = 220
BADGE_HEIGHT = 50
BG_COLOR = "#2c3e50"
TEXT_COLOR = "#ffffff"
FONT_SIZE = 18
# =======================================

# 统一使用北京时间计算，避免时区误差
beijing_tz = ZoneInfo("Asia/Shanghai")
today = datetime.now(beijing_tz).date()
last_date = datetime.strptime(LAST_UPDATE_DATE, "%Y-%m-%d").date()

# 计算整数天数差
days_since = (today - last_date).days

if days_since == 0:
    display_text = "今天更新"
else:
    display_text = f"{LABEL_TEXT} {days_since} {SUFFIX_TEXT}"

# 生成 SVG 图片
svg_content = f'''<svg width="{BADGE_WIDTH}" height="{BADGE_HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{BADGE_WIDTH}" height="{BADGE_HEIGHT}" rx="8" fill="{BG_COLOR}"/>
  <text x="{BADGE_WIDTH//2}" y="{BADGE_HEIGHT//2 + 6}" 
        font-family="Arial, 'Microsoft YaHei', sans-serif" 
        font-size="{FONT_SIZE}" 
        fill="{TEXT_COLOR}" 
        text-anchor="middle">
    {display_text}
  </text>
</svg>'''

# 保存为图片文件
with open("badge.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

import cairosvg
cairosvg.svg2png(bytestring=svg_content.encode("utf-8"), write_to="badge.png")
