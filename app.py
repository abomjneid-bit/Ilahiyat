import os
import gradio as gr

MOVIES = [
    {"title": "فيلم وثائقي: تاريخ الحواسيب", "genre": "وثائقي", "size": "1.2 GB"},
    {"title": "فيلم أنيميشن مغامرات رائع", "genre": "رسوم متحركة", "size": "850 MB"}
]

BOOKS = [
    {"title": "تعلم شبكات ميكروتك من الصفر", "author": "م. أحمد", "category": "تقنية"},
    {"title": "دليل البرمجة بلغة بايثون للأنظمة المدمجة", "author": "د. خالد", "category": "برمجة"}
]

GAMES = [
    {"name": "Super Mario (Offline Web)", "type": "منصات / كلاسيك", "size": "15 MB", "play_type": "تشغيل مباشر في المتصفح"},
    {"name": "Counter Strike 1.6 (Portable)", "type": "تصويب / أكشن", "size": "250 MB", "play_type": "تحميل وتشغيل أوفلاين"}
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
    gr.Markdown("# 🌐 منصة الخدمات الرقمية للشبكة المحلية (أوفلاين)")
    gr.Markdown("### محاكاة تجريبية للنظام المخطط لتشغيله عبر الهارد ديسك والراوتر")
    
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

    with gr.Tab("🎮 منصة الألعاب"):
        gr.Markdown("### 🕹️ مركز ألعاب الشبكة (تحميل مباشر وتشغيل فوراً)")
        for game in GAMES:
            with gr.Row():
                gr.Markdown(f"🎮 **{game['name']}** — *النوع:* {game['type']} — *الحجم:* {game['size']}")
                gr.Button(f"🚀 {game['play_type']}")

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

# تعديل أمر الإطلاق ليتناسب مع متغيرات منافذ خادم Render الديناميكية
if __name__ == "__main__":
    server_port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=server_port, theme=gr.themes.Soft())
