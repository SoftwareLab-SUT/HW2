# آزمایش دوم: مدیریت نسخ پروژه و یکپارچه‌سازی مستمر
مهرانه نجفی (۹۷۱۰۴۷۰۷)، رستا روغنی(۹۷۱۰۵۹۶۳) 

**مراحل انجام پروژه**  
ابتدا کد main موجود در شاخه‌ی اصلی زده‌شد که در آن از کاربر زبان ورودی‌اش را گرفته و به او سلام می‌کنیم.  
پس از آن سه شاخه‌ی Song-Recommendation و Zodiac-Sign و Daily-Horoscope ساخته‌شدند که در هر کدام یک فیچر به main اضافه می‌شود:  
در Song-Recommendation از کاربر مود آن روزش را گرفته و یک آهنگ متناسب برمی‌گرداند. 
در Zodiac-Sign از کاربر ماه تولد گرفته و علامت زودیاک آن را برمی‌گرداند.
در Daily-Horoscope هم از کاربر ماه تولدش را گرفته و فال امروزش را برمی‌گرداند.
همانطور که در فایل‌ها هم می‌بینید gitignore داریم که در آن لیستی از فایل‌ها که نمی‌خواهیم گیت تغییرات آن‌ها را پیگیری کند، در آن قرار دادیم مانند idea/*.

شاخه‌ی main ما protected است و برای اینکه بتوان تغییرات شاخه‌های دیگر را به آن اضافه کرد، باد pull request فرستاد که در شکل زیر هم می‌بینید:

دو بار درطول پروژه ما conflict خوردیم که یک بار مربوط به زمانی بود که در شاخه‌ی Song-Recommendation هردو نفر تلاش کردیم آهنگ‌های موجود را عوض کنیم که بعد از اجرای دستور git push توسط نفر دوم، نتیجه‌ی زیر داده‌شد و با مرج کردن دو کد، مشکل برطرف شد: 

<img width="1264" alt="Screen Shot 1401-08-20 at 19 26 15" src="https://user-images.githubusercontent.com/45355352/201385111-b6ca544f-f50b-48c5-b85b-ab0b52b491c0.png">


**پاسخ سوالات دستورکار** 

۱.پوشه‌ی .git چیست؟ چه اطلاعاتی در آن ذخیره میشود؟

پس از اجرای دستور git init این پوشه ساخته می‌شود که در حالت عادی پنهان است تا کسی به‌صورت تصادفی آن را پاک نکند و یا تغییری ندهد.
این پوشه تمامی اطلاعات ضروری پروژه و اطلاعات مربوط به version control، remote repository address و کامیت‌ها را دربر می‌گیرد.
همچنین در آن لاگی قرار دارد که تاریخچه‌ی کامیت‌ها را ذخیره می‌کند که در زمانی که بخواهیم به یکی از کامیت‌های قبلی برگردیم، به کار می‌آید چون اسنپ‌شات‌های کامیت‌ها موجود هستند. در داخل پوشه‌ی .git پوشه‌های دیگری قرار دارند که در ادامه به مختصر آن‌ها را توضیح می‌دهیم:
- پوشه hooks: فایل‌های اسکریپت را دربر می‌گیرد که به Git Hook Scripts معروف هستند. این اسکریپت‌ها قبل یا بعد وقوع eventهایی مثل کامیت، پوش یا  پول اجرا می‌شوند.
- پوشه objects: در گیت همه‌چیز به عنوان شی نگهداری می‌شود و این پوشه یک پایگاه داده برای آن‌هاست.
- فایل config: یک configuration file لوکال است که اطلاعاتی همچون ایمیل و نام کاربری را ذخیره می‌کند. 
- پوشه refs: اطلاعات مربوط به تگ‌ها و شاخه‌ها در این پوشه نگهداری می‌شود.
- فایل HEAD: این فایل اشاره‌گری به شاخه‌ی کنونی را نگه می‌دارد که به صورت پیش‌فرض به شاخه‌ی master اشاره‌ می‌کند. 
- فایل index: یک فایل باینری است که اطلاعات staging را نگه می‌دارد. 
- پوشه info: این پوشه فایل exclude را دربر می‌گیرد که که شامل پترن‌های است که نمی‌خواهیم گیت آن‌ها را بخواند و یا اجرا کند.

۲.منظور از atomic بودن کامیت و pull request چیست؟

منظور از atomic بودن pull request و کامیت این است که
همواره یا به‌طور کامل انجام می‌شوند (succeed) و یا کلا انجام نمی‌شوند (fail).
بنابراین اگر درهنگام انجام این دو عملیات مشکلی ایجاد شود، تمامی تغییراتی که تا آن لحظه اعمال شده‌بودند، حذف می‌شوند و پروژه به حالت قبلی برمی‌گردد یا اگر مشکلی ایجاد نشود، تمامی تغییراتی که مدنظر بوده‌اند روی پروژه اعمال می‌شوند. هدف از این ویژگی این است که سیسستم همواره در یک حالت پایدار قرار داشته‌باشد. 
به‌ زبان دیگر، کامیت‌ها و pull requestها به شکل isolated هستند و امکان انجام هم‌زمان دو یا تعداد بیشتری عملیات کامیت (یا پول) وجود ندارد. 
درضمن ویژگی‌های زیر هم از atomic بودن کامیت و pull request نتیجه می‌شوند:  
- می‌توان آن‌ها را revert کرد بدون آنکه نتایج ناخواسته‌ای داشته‌باشند.
بطور مثال اگر یک کامیت از تاریخچه‌ی کامیت‌ها حذف شود اما باعث تغییراتی جز آنچه در پیام کامیت نوشته‌شده‌است، بشود، atomic نیست. 
- کامیت atomic را باید بتوان با یک پیام ساده توصیف کرد بدون آنکه نیاز باشد درمورد کارهای نامرتبط دیگری که انجام شده‌اند، توضیح داد. درواقع هرکامیت فقط باید تغییرات مربوط به یک unit را دربربگیرد.
هر pull request هم می‌تواند شامل یک یا تعداد بیشتری atomic کامیت باشد.

۳.تفاوت دستورهای fetch و pull و merge را بیان کنید. مثال بزنید.

دستور merge: تغییراتی که توسط کامیت‌های مدنظر داده‌شده را (از زمانی که تاریخچه‌شان از شاخه‌ی کنونی جدا شده) به روی شاخه‌ی کنونی اعمال می‌کند. 
همچنین اگر دستور git merge از روی یک شاخه بر روی شاخه‌ی دیگری اجرا شود به این معنا است که تغییرات شاخه دوم رو روی شاخه اول اعمال کن.
دستور git pull هم از merge برای گرفتن تغییرات یک شاخه استفاده می‌کند.
مثال: فرض کنید در حال حاضر روی شاخه‌ی master هستیم و کامیت‌ها به شکل زیر هستند: 

 <img width="243" alt="Screen Shot 1401-08-20 at 13 03 09" src="https://user-images.githubusercontent.com/45355352/201310812-7aa34c3f-ed04-454a-a7d2-90159c870ff5.png">
 
در این‌صورت پس از اجرای دستور git merge topic، تمامی تغییراتی که روی شاخه‌ی topic از زمان کامیت E تا کامیت C داده‌شده به شکل یک کامیت در می‌آیند.
نتیجه‌ به شکل زیر می‌شود:

<img width="251" alt="Screen Shot 1401-08-20 at 13 07 31" src="https://user-images.githubusercontent.com/45355352/201311699-7fce51f4-e361-4985-a752-aa4be6c77ec3.png">  

دستور fetch: این دستور تغییرات کامیت‌ها، refها و فایل‌ها رو از repository ریموت دریافت میکند ولی هیچ تغییری روی برنچ های local‌ اعمال نمیکند. بنابراین کد ما تغییری نمی‌کند که این تفاوتش با دستور git pull است.
مثال: فرض کنید که دو ریپازیتوری زیر را داریم:

<img width="336" alt="Screen Shot 1401-08-20 at 13 28 33" src="https://user-images.githubusercontent.com/45355352/201315936-4e027c03-25b1-43af-8ff7-bcda051687a2.png">

در این صورت پس از اجرا کردن دستور git fetch، گیت تفاوت‌هایی که repository لوکال نسبت به ریموت دارد را در شاخه‌ای با نام remote-name/branch-name، ذخیره می‌کند.

دستور pull: این دستور تغییرات داده‌شده بر روی یک remote repository را وارد شاخه‌ کنونی می‌کند.
به این منظور ابتدا دستور git fetch اجرا می‌شود تا کپی‌ای از تفاوت شاخه‌ها ذخیره شود. بعد از آن دو حالت داریم:

- شاخه‌ی کنونی از شاخه‌ی remote عقب‌تر باشد که در این صورت آن را جلو می‌برد تا به آخرین کامیت remote برسد.
- شاخه‌ی کنونی و شاخه‌ی remote از هم جدا شده‌باشند (مسیرهای مختلفی رفته‌باشند) که در این صورت براساس پرچم‌ها و configuration، یکی از دو دستور git rebase یا git merge اجرا می‌شوند.

مثال: فرض کنید در حال حاضر روی شاخه‌ی master هستیم و کامیت‌ها به شکل زیر هستند:

<img width="358" alt="Screen Shot 1401-08-20 at 13 20 36" src="https://user-images.githubusercontent.com/45355352/201314476-6b5c775f-1500-4afb-abaf-320ef5715152.png">

پس از اجرای دستور git pull، تغییرات داده‌شده به روی remote master از زمان جدا شدنش (کامیت E) تا آخرین کامیت (کامیت C) به شکل یک کامیت درمی‌آیند و به شاخه‌ی master داده می‌شوند:

<img width="271" alt="Screen Shot 1401-08-20 at 13 23 47" src="https://user-images.githubusercontent.com/45355352/201315008-9cc1aa90-642d-4397-8d28-a09adccbdcf1.png">

تفاوت این دستور‌ها را در شکل‌های زیر نیز می‌توان مشاهده کرد:

![image](https://user-images.githubusercontent.com/45355352/201318799-c2c60c00-5e70-4148-978d-d4be541ed0ad.png)
![image](https://user-images.githubusercontent.com/45355352/201319694-f9cfde51-5fae-41ee-9c70-9582bbdd12f4.png)

۴.تفاوت دستورهای rebase و clone را بیان کنید. مثال بزنید.

دستور clone:
clone کردن یک مخزن، درواقع کپی کردن آن مخزن است. هنگامی که یک مخزن ریموت داریم و دستور git clone‌را برای url آن مخزن می‌زنیم، یک کپی محلی از آن مخزن برای ما درست می‌شود. یک clone، تمامی فایل‌ها، شاخه‌ی master و تمامی شاخه‌های دیگر ، کامیت‌ها و ... را در بر دارد. تمامی تغییراتی که لوکال روی لپ‌تاپ خود برای این مخزن انجام می‌دهیم روی این clone انجام می‌شود و سپس این تغییرات پس از کامیت شدن روی مخزن ریموت push می‌شوند.

دستور rebase:

۵.تفاوت دستورهای reset و revert را بیان کنید. مثال بزنید.
فرض کنید کامیت‌های زیر را داریم:

![git-reset](https://user-images.githubusercontent.com/56794518/201332776-c935f8ea-ad76-48a5-aea8-349db4e500ca.jpg)

کامیت‌های A و B کامیت‌های درستی‌اند ولی فرضا اشتباهی در کامیت C و D‌ پیش آمده که می‌خواهیم از آن‌ها به کامیت B برگردیم. فعلا سر اشاره روی کامیت D است و باید HEAD را به کامیت B a0fvf8 اشاره دهیم. با دستور:
```sh
$ git reset --hard a0fvf8
```

اکنون HEAD‌ به کامیت B اشاره می‌کند و کامیت‌ها به شکل زیر خواهند بود:

![git-reset-2](https://user-images.githubusercontent.com/56794518/201333550-dc9821f3-3e60-4152-b812-31f0aaf73b4c.jpg)

اما در revert یک کامیت جدید تولید می‌شود که به یک کامیت در گذشته برمی‌گردد و پس از این کار HEAD به کامیت جدید اشاره می‌کند. مثلا در مثالی که کمی بالاتر زدیم می‌توانستیم اول کامیت D را revert کنیم و سپس کامیت C را. پس از اجرای دستورات revert زیر کامیت‌ها به شکل زیر می‌شوند:
```sh
$ git revert 5lk4er
$ git revert 76sdeb
```

![git-revert](https://user-images.githubusercontent.com/56794518/201335517-727a7e49-06e5-44e4-97be-79984aeb2c96.jpg)

در صورتی که تعداد کامیت‌هایی که بخواهیم revert کنیم زیاد باشند می‌توانیم‌ رنجی از کامیت‌ها را برای revert کردن مشخص کنیم:

```sh
$ git revert OLDER_COMMIT^..NEWER_COMMIT
```

۶.منظور از stage و snapshot چیست؟

مفهوم stage یک قدم پیش از کامیت است. تا زمانی که تغییرات در حالت stage باشند می‌توانید تغییرات خود را اعمال کنید اما پس از اینکه از این حالت گذر کنیم دیگر کار کامیت آغاز می‌شود. در حالت staging به گیت اطلاع می‌دهید که چه تغییراتی را می‌خواهیم با این کامیت به مخزن انتقال دهیم و چه تغییراتی فعلا در این کامیت منتقل نشوند.

هر دفعه‌ای که به یک مخزن کامیت می‌کنیم، یک snapshot از فایل‌های فعلی مخزن تشکیل می‌شود که حالت فعلی تمامی فایل‌ها را در این زمان ذخیره می‌کند. وقتی می‌خواهیم یک شاخه‌ی جدید تشکیل دهیم و از git checkout -b new-branch استفاده می‌کنیم، گیت یک snapshot از فایل‌های فعلی در شاخه‌ی فعلی تشکیل می‌دهد و از روی آن شاخه‌ی جدید را می‌سازد؛ مانند عکسی که از یک واقعه با تمامی جزئیات گرفته می‌شود تا صحنه‌ی آن در آینده بتواند بازسازی شود. با استفاده از snapshot می‌توانیم به کامیت‌های گذشته (یعنی حالت‌های گذشته که ذخیره شده‌اند) برگردیم.
