@echo off
chcp 65001 >nul
cd /d "D:\ZM\yizqzk-docs"

echo ============================
echo  YizMod QZK 文档站
echo ============================

echo.
echo [1/3] 生成 API 文档...
python scripts\generate_api_docs.py

echo.
echo [2/3] 生成变更日志...
python scripts\update_changelog.py

echo.
echo [3/3] 导出 LLM 知识库...
python scripts\export_llm.py

echo.
echo ============================
echo  启动本地服务器...
echo  打开浏览器访问:
echo    http://localhost:8080
echo ============================
echo.
echo  按 Ctrl+C 停止服务器
echo.

mkdocs serve -a 0.0.0.0:8080
pause
