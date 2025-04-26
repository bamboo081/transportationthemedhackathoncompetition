# frontend/Dockerfile
FROM node:18-alpine

# Install dependencies
WORKDIR /app
COPY frontend/package.json frontend/package-lock.json* ./
RUN npm ci --production

# Copy the rest of the frontend
COPY frontend/ .

# Build the Next.js app
RUN npm run build

# Expose the Next.js port
EXPOSE 3000

# Start in production mode
CMD ["npm", "start"]