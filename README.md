# Profile Project

這是一個使用 Ubuntu Server、Docker、Flask 與 MongoDB 建立的個人資料管理練習專案。

本專案包含個人資料顯示頁面以及個人資料修改頁面，前端透過 API 與後端連線，資料儲存在 MongoDB 資料庫中。

## 系統架構

- Ubuntu Server：伺服器環境
- SSH：遠端連線與開發
- Git / GitHub：版本控制
- Docker / Docker Compose：容器化部署
- Python Flask：後端 API
- MongoDB：NoSQL 資料庫
- HTML / CSS / JavaScript：前端網頁

## 專案結構

profile-project/

- backend/
  - app.py
  - Dockerfile
  - requirements.txt
- frontend/
  - index.html
  - edit.html
- compose.yaml
- .gitignore
- README.md

## 功能

### 個人資料頁面

顯示以下個人資料：

- 姓名
- 學號
- 系所
- 電子郵件
- 關於我

### 修改個人資料頁面

可以修改個人資料，更新後會透過後端 API 將資料儲存至 MongoDB。

## API

取得個人資料：

GET /api/profile

更新個人資料：

PUT /api/profile

資料格式使用 JSON。

## Docker

後端與 MongoDB 使用 Docker 容器執行。

啟動：

```bash
docker compose up -d
