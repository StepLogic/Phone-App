FROM node:16.0.0-alpine3.13
WORKDIR /frontend
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000