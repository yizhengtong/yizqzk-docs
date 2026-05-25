@echo off
chcp 65001 >nul
cd /d "D:\ZM\yizgzq\yizqzk-docs"

echo ============================
echo  YizMod QZK 文档站
echo ============================

echo.
echo [1/4] 启动天赋推送服务 (localhost:8765)...
start "天赋推送服务" cmd /c "python scripts\talent_server.py"

echo.
echo [2/4] 生成 API 文档...
python scripts\generate_api_docs.py

echo.
echo [3/4] 生成变更日志...
python scripts\update_changelog.py

echo.
echo [4/4] 导出 LLM 知识库...
python scripts\export_llm.py

echo.
echo ============================
echo  启动本地服务器...
echo.
echo  文档站: http://localhost:8080
echo  天赋构造器: http://localhost:8080/tools/talent-builder/
echo  推送收件箱: D:\ZM\yizgzq\_talent-inbox\
echo ============================
echo.
echo  按 Ctrl+C 停止文档站
echo  关闭「天赋推送服务」窗口停止推送服务
echo.

mkdocs serve -a 0.0.0.0:8080
pause
