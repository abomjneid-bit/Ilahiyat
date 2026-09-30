import os
import gradio as gr

# قائمة الألعاب الكلاسيكية مع روابط المحاكيات المباشرة (Emulators)
ARCADE_GAMES = [
    {
        "name": "FIFA / Winning Eleven (كلاسيك جماعي)", 
        "system": "PlayStation 1", 
        "players": "1 - 4 لاعبين (جماعي محلي)",
        "embed_url": "https://emulatorjs.org"  # رابط تجريبي للمحاكي
    },
    {
        "name": "WWF SmackDown! 2 (مصارعة التحدي)", 
        "system": "PlayStation 1", 
        "players": "1 - 4 لاعبين (جماعي محلي)",
        "embed_url": "https://emulatorjs.org"
    },
    {
        "name": "Call of Duty: Roads to Victory", 
        "system": "Retro Classic", 
        "players": "جماعي عبر الشبكة المحلية",
        "embed_url": "https://emulatorjs.org"
    },
    {
        "name": "Mortal Kombat / Street Fighter", 
        "system": "Sega Mega Drive", 
        "players": "لاعبين اثنين (Versus)",
        "embed_url": "https://emulatorjs.org"
    }
]

MOVIES = [
    {"title": "فيلم وثائقي: تاريخ الحواسيب", "genre": "وثائقي", "size": "1.2 GB"},
    {"title": "فيلم أنيميشن مغامرات رائع", "genre": "رسوم متحركة", "size": "850 MB"}
]

BOOKS = [
    {"title": "تعلم شبكات ميكروتك من الصفر", "author": "م. أحمد", "category": "تقنية"},
    {"title": "دليل البرمجة بلغة بايثون للأنظمة المدمجة", "author": "د. خالد", "category": "برمجة"}
]

PRODUCTS = [
    {"name": "راوتر ميكروتك hAP lite مُعد مسبقاً", "price": "1200 TL", "stock": "متوفر 5 قطع"},
    {"name": "باور بانك ذكي 20,000mAh مخارج متعددة", "price": "850 TL", "stock": "متوفر قطعتين"}
]

def buy_product(product_name):
    return f"🛒 تم استلام طلبك لـ ({product_name}) بنجاح! سيتم معالجة الطلب عبر الشبكة المحلية قريباً."

def play_movie(movie_title):
    return f"🎬 جاري تشغيل وبث ({movie_title}) الآن من الهارد ديسك المحلي للشبكة..."

with gr.Blocks(title="منصة الشبكة المحلية المعزولة") as demo:
    gr.Markdown("# 🌐 منصة الخدمات الرقمية وصالة الألعاب المحلية (أوفلاين)")
    gr.Markdown("### 🕹️ العب مباشرة مع أصدقائك عبر المتصفح بدون تحميل وبدون إنترنت!")
    
    with gr.Tab("🎮 صالة ألعاب المتصفح الجماعية"):
        gr.Markdown("### 🕹️ اختر لعبتك المفضلة والعب فوراً عبر شبكة الواي فاي")
        
        for game in ARCADE_GAMES:
            with gr.Group():
                gr.Markdown(f"## 🎮 {game['name']}")
                gr.Markdown(f"**الجهاز الأصلي:** {game['system']} | **نمط اللعب:** {game['players']}")
                
                # تضمين المحاكي داخل الواجهة مباشرة ليظهر كشاشة لعبة حقيقية
                gr.HTML(f"""
                <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 8px; border: 2px solid #4F46E5;">
                    <iframe src="{game['embed_url']}" 
                            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
                            allowfullscreen 
                            allow="gamepad">
                    </iframe>
                </div>
                """)
                gr.Markdown("ℹ️ *تنبيه:* المنصة تدعم توصيل **أذرع التحكم (Gamepads/Joysticks)** بالهاتف أو الكمبيوتر مباشرة عبر البلوتوث أو الـ USB للعب الجماعي.")
                gr.Markdown("---")

    with gr.Tab("🎬 منصة الأفلام والمديا"):
        gr.Markdown("### 🎥 شاهد الأفلام مباشرة من الهارد ديسك المحلي بدون إنترنت")
        for movie in MOVIES:
            with gr.Group():
                gr.Markdown(f"### 🎞️ {movie['title']}")
                gr.Markdown(f"**التصنيف:** {movie['genre']} | **الحجم:** {movie['size']}")
                play_btn = gr.Button("▶️ تشغيل الفيلم الآن عبر الشبكة LOCAL")
                movie_status = gr.Textbox(label="حالة البث والتوصيل", interactive=False)
                play_btn.click(fn=play_movie, inputs=gr.State(movie['title']), outputs=movie_status)
                gr.Markdown("---")
                
    with gr.Tab("📚 المكتبة الرقمية"):
        gr.Markdown("### 📖 تصفح وحمّل الكتب والملفات التعليمية مجاناً")
        with gr.Row():
            for book in BOOKS:
                with gr.Column(scale=1):
                    gr.Markdown(f"### 📘 {book['title']}")
                    gr.Markdown(f"**المؤلف:** {book['author']}\n\n**القسم:** {book['category']}")
                    gr.Button("⬇️ تحميل الكتاب أوفلاين")

    with gr.Tab("🛒 المتجر الإلكتروني المحلي"):
        gr.Markdown("### 🛍️ متجر الشبكة لشراء المنتجات والخدمات الرقمية")
        with gr.Row():
            for prod in PRODUCTS:
                with gr.Column():
                    gr.Markdown(f"### {prod['name']}")
                    gr.Markdown(f"**السعر:** {prod['price']} \n\n**حالة المخزن:** {prod['stock']}")
                    btn = gr.Button("🛒 شراء الآن", variant="primary")
                    output_status = gr.Textbox(label="حالة الطلب", interactive=False)
                    btn.click(fn=buy_product, inputs=gr.State(prod['name']), outputs=output_status)

if __name__ == "__main__":
    server_port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=server_port, theme=gr.themes.Soft())
