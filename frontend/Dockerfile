FROM node:20-alpine
WORKDIR /teleposter
COPY package*.json ./
RUN npm install
COPY ./public ./public
COPY ./src ./src
CMD ["npm", "run", "build"]