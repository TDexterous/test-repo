# official python runtime
FROM python:3.11-slim

# set cwd
WORKDIR /app

# copy cwd content into container
COPY . .

# install deps
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run the app with gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:3000", "app:app"]
