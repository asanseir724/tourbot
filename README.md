برای نصب کل پروژه با یک خط کد، می‌توانید از دستورات زیر استفاده کنید که مخزن را کلون کرده، وارد پوشه پروژه می‌شود، و پیش‌نیازها را نصب می‌کند:

bash
Copy code
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git && cd YOUR_REPOSITORY && pip install -r requirements.txt
توضیحات:
git clone: مخزن پروژه را از GitHub دانلود می‌کند.
cd YOUR_REPOSITORY: وارد پوشه پروژه می‌شود.
pip install -r requirements.txt: تمام پیش‌نیازهای پروژه را نصب می‌کند.
با اجرای این خط کد، تمام تنظیمات و پیش‌نیازهای پروژه به‌صورت خودکار نصب می‌شود و می‌توانید بلافاصله پس از آن ربات را اجرا کنید.
