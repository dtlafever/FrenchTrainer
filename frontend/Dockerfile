FROM node:22.14.0-slim

WORKDIR /app

# Copy package files
COPY frontend/package.json frontend/package-lock.json ./

# Install dependencies
RUN npm ci

# Copy frontend code
COPY frontend/ ./

# Build the application
RUN npm run build

# Use nginx to serve static files
FROM nginx:alpine

# Copy built assets from builder stage
COPY --from=0 /app/dist /usr/share/nginx/html

# Copy nginx configuration
COPY frontend/nginx.conf /etc/nginx/conf.d/default.conf

# Expose port
EXPOSE 80

# Command to run nginx
CMD ["nginx", "-g", "daemon off;"]