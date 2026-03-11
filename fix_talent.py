#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
統一第 1-40 章天賦名稱為「魔法之源」
"""

import os
import re

# 定義兩個目錄
DIRS = [
    "/home/novel/.openclaw/workspace/chapters",
    "/home/novel/.openclaw/workspace/Novel_wo_yong_xin_shou_mu_jian_shi_shen/chapters"
]

# 標準天賦描述格式
STANDARD_TALENT_BLOCK = """【超神級天賦·魔法之源】
效果 a：技能效果提高 100%
效果 b：增益持續時間提高 10 倍
效果 c：技能冷卻降低 80%
效果 d：全屬性提高 100%，智力精神再額外提高 100%
效果 e：相同增益可疊加時間"""

# 需要替換的模式
REPLACEMENTS = [
    # 天賦名稱統一
    (r'【天賦：法神遗孤（超神级）】', '【超神級天賦·魔法之源】'),
    (r'【天賦：超神級（被動）】', '【超神級天賦·魔法之源】'),
    (r'【天賦：超神級（唯一）】', '【超神級天賦·魔法之源】'),
    (r'【天賦：特殊天賦（效果：技能效果提高 100%、增益持續時間提高 10 倍、技能冷卻降低 80%、全屬性提高 100%）】', '【超神級天賦·魔法之源】'),
    (r'【天賦效果：智力×2×3=360，精神×2×3=360】', ''),
    
    # 天賦效果列表格式統一（多種變體）
    (r'【超神級天賦·魔法之源（被動）】', '【超神級天賦·魔法之源】'),
    (r'【魔法之源·效果 a：技能效果提高 100%】', '效果 a：技能效果提高 100%'),
    (r'【魔法之源·效果 b：增益持續時間提高 10 倍】', '效果 b：增益持續時間提高 10 倍'),
    (r'【魔法之源·效果 c：技能冷卻降低 80%】', '效果 c：技能冷卻降低 80%'),
    (r'【魔法之源·效果 d：全屬性提高 100%，智力精神再額外提高 100%】', '效果 d：全屬性提高 100%，智力精神再額外提高 100%'),
    (r'【魔法之源·效果 e：相同增益可疊加時間】', '效果 e：相同增益可疊加時間'),
    
    # 帶縮進和列表符的效果
    (r'  - a: 技能效果提高 100%\n  - b: 增益持續時間提高 10 倍\n  - c: 技能冷卻降低 80%\n  - d: 全屬性提高 100%，智力精神再額外提高 100%\n  - e: 相同增益可疊加時間', 
     '效果 a：技能效果提高 100%\n效果 b：增益持續時間提高 10 倍\n效果 c：技能冷卻降低 80%\n效果 d：全屬性提高 100%，智力精神再額外提高 100%\n效果 e：相同增益可疊加時間'),
    
    # 簡寫版本
    (r'a: 技能效果提高 100%\nb: 增益持續時間提高 10 倍\nc: 技能冷卻降低 80%\nd: 全屬性提高 100%，智力精神再額外提高 100%\ne: 相同增益可疊加時間',
     '效果 a：技能效果提高 100%\n效果 b：增益持續時間提高 10 倍\n效果 c：技能冷卻降低 80%\n效果 d：全屬性提高 100%，智力精神再額外提高 100%\n效果 e：相同增益可疊加時間'),
]

# 需要刪除的天罰相關描述
TIANFA_PATTERNS = [
    r'天罰之手',
    r'天罰',
]

def process_file(filepath):
    """處理單個文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 應用所有替換
    for pattern, replacement in REPLACEMENTS:
        content = re.sub(pattern, replacement, content)
    
    # 檢查是否有修改
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    total_files = 0
    modified_files = 0
    
    for dir_path in DIRS:
        if not os.path.exists(dir_path):
            print(f"目錄不存在：{dir_path}")
            continue
        
        for i in range(1, 41):
            filename = f"chapter_{i:02d}.md"
            filepath = os.path.join(dir_path, filename)
            
            if os.path.exists(filepath):
                total_files += 1
                if process_file(filepath):
                    modified_files += 1
                    print(f"已修改：{filepath}")
    
    print(f"\n處理完成：共 {total_files} 個文件，修改了 {modified_files} 個文件")

if __name__ == "__main__":
    main()
