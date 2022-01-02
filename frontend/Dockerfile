FROM node:16-alpine
WORKDIR /app

COPY package.json package-lock.json ./
RUN npm i

EXPOSE 3000
ENV PORT 3000

ENTRYPOINT ["node_modules/.bin/next", "dev"]
