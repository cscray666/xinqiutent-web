const fs = require('fs');

const data = JSON.parse(fs.readFileSync('scraped_products_full.json', 'utf8'));

const nav = `
                <div class="hidden md:flex space-x-6 text-xs font-semibold uppercase tracking-wider items-center">
                    <a href="index.html" class="hover:text-blue-600 transition">Home</a>
                    <a href="camping-tents.html" class="hover:text-blue-600 transition">Camping</a>
                    <a href="pop-up-tents.html" class="hover:text-blue-600 transition">Pop-up</a>
                    <a href="changing-tents.html" class="hover:text-blue-600 transition">Changing</a>
                    <a href="roof-top-tents.html" class="hover:text-blue-600 transition">Rooftop</a>
                    <a href="beach-tents.html" class="hover:text-blue-600 transition">Beach</a>
                    <a href="outdoor-furniture.html" class="hover:text-blue-600 transition">Furniture</a>
                    <a href="inflatable-tents.html" class="hover:text-blue-600 transition">Inflatable</a>
                    <a href="about.html" class="hover:text-blue-600 transition">Our Soul</a>
                    <a href="index.html#news" class="hover:text-blue-600 transition">Intelligence</a>
                    <a href="index.html#contact" class="px-5 py-2 bg-blue-600 text-white rounded-full hover:bg-blue-700 transition">Inquiry</a>
                </div>
`;

const footer = `
    <footer class="bg-gray-900 text-white py-16 text-center text-sm border-t border-slate-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-center space-x-8 mb-8 text-2xl text-slate-400">
                <a href="https://www.linkedin.com/company/ningbo-xinqiu-travelling-products-co-ltd/" target="_blank" class="hover:text-blue-500 transition" title="LinkedIn Company Page"><i class="fab fa-linkedin"></i></a>
                <a href="https://www.linkedin.com/in/shichen-cheng" target="_blank" class="hover:text-blue-400 transition" title="LinkedIn Personal Profile"><i class="far fa-id-card"></i></a>
                <a href="https://www.instagram.com/windvalleyoutdoor/" target="_blank" class="hover:text-pink-500 transition" title="Instagram Business Page"><i class="fab fa-instagram"></i></a>
                <a href="https://www.instagram.com/crsacy?igsh=MWF4eWpsZjduZXJ3dw%3D%3D&utm_source=qr" target="_blank" class="hover:text-pink-400 transition" title="Instagram Personal Profile"><i class="far fa-user-circle"></i></a>
                <a href="https://www.tiktok.com/@windvalleyoutdoor?_r=1&_t=ZT-974T2xMVl1B" target="_blank" class="hover:text-slate-100 transition" title="TikTok Page"><i class="fab fa-tiktok"></i></a>
                <a href="https://www.facebook.com/share/18nmvYHjVt/?mibextid=wwXIfr" target="_blank" class="hover:text-blue-600 transition" title="Facebook Page"><i class="fab fa-facebook"></i></a>
            </div>
            <p class="opacity-60">&copy; 2026 Ningbo Xinqiu Travelling Products Co., Ltd. All rights reserved.</p>
        </div>
    </footer>
    <!-- WhatsApp Floating Button -->
    <a href="https://wa.me/8618989341689" target="_blank" class="fixed bottom-8 right-8 z-[100] bg-green-500 text-white p-4 rounded-full shadow-2xl hover:bg-green-600 transition-all group flex items-center space-x-2">
        <i class="fab fa-whatsapp text-2xl"></i>
        <span class="max-w-0 overflow-hidden group-hover:max-w-xs transition-all duration-500 ease-in-out whitespace-nowrap font-bold">Chat with Factory Manager</span>
    </a>
`;

function getHead(title, description) {
    return `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title} - Premium OEM Factory | Ningbo Xinqiu</title>
    <meta name="description" content="${description}">
    
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-BBBEBVF9BX"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-BBBEBVF9BX');
    </script>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        body { font-family: 'Inter', sans-serif; }
    </style>
</head>
<body class="bg-gray-50">
    <nav class="fixed w-full z-50 bg-white/90 backdrop-blur-md border-b">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-20 items-center">
                <div class="flex-shrink-0 flex items-center">
                    <a href="index.html" class="text-2xl font-bold text-blue-900">XINQIU <span class="text-blue-600">TENT</span></a>
                </div>
                ${nav}
            </div>
        </div>
    </nav>
`;
}

function generateProductCard(p, index) {
    let cleanName = p.name.replace(/[\u4e00-\u9fa5]/g, '').trim();
    if (!cleanName) cleanName = "Professional Product " + (index + 1);
    
    if (p.is_expert_style) {
        return `
                <!-- B2B Expert Style (LuxoPack Inspired) -->
                <div class="col-span-full lg:col-span-2 bg-slate-900 rounded-[2rem] overflow-hidden flex flex-col md:flex-row shadow-2xl border border-slate-800 group transition-all duration-500 hover:border-blue-500/50">
                    <div class="md:w-1/2 h-[400px] md:h-auto bg-slate-800/50 p-8 flex items-center justify-center">
                        <img src="${p.img.replace('_200x200.jpg', '_640x640.jpg')}" alt="${cleanName}" class="w-full h-full object-contain group-hover:scale-105 transition duration-700">
                    </div>
                    <div class="md:w-1/2 p-10 flex flex-col justify-between">
                        <div>
                            <div class="inline-flex items-center gap-2 px-3 py-1 bg-blue-500/10 text-blue-400 rounded-full text-[10px] font-black uppercase tracking-widest mb-6">
                                <i class="fas fa-cube"></i> Premium Selection
                            </div>
                            <h3 class="text-3xl font-bold text-white mb-6 leading-tight">${cleanName}</h3>
                            <p class="text-slate-400 text-sm leading-relaxed mb-8">${p.description || ''}</p>
                            
                            <div class="grid grid-cols-3 gap-6 py-8 border-y border-slate-800/50 mb-8">
                                <div>
                                    <div class="text-slate-500 text-[9px] font-black uppercase tracking-tighter mb-1">MOQ</div>
                                    <div class="text-white text-xs font-bold whitespace-nowrap">${p.moq}</div>
                                </div>
                                <div>
                                    <div class="text-slate-500 text-[9px] font-black uppercase tracking-tighter mb-1">LEAD TIME</div>
                                    <div class="text-white text-xs font-bold whitespace-nowrap">${p.lead_time || '30 Days'}</div>
                                </div>
                                <div>
                                    <div class="text-slate-500 text-[9px] font-black uppercase tracking-tighter mb-1">MATERIAL</div>
                                    <div class="text-white text-xs font-bold whitespace-nowrap">${p.material || 'Heavy Duty'}</div>
                                </div>
                            </div>
                        </div>
                        
                        <a href="index.html#contact" class="w-full py-4 rounded-xl border-2 border-blue-500/30 text-blue-400 font-black text-xs uppercase tracking-widest flex items-center justify-center gap-3 hover:bg-blue-600 hover:text-white hover:border-blue-600 transition-all duration-300">
                            Get A Free Quote <i class="fas fa-arrow-right text-[10px]"></i>
                        </a>
                    </div>
                </div>
        `;
    }

    return `
                <div class="bg-white rounded-2xl shadow-sm border p-6 hover:shadow-xl transition group">
                    <div class="h-72 rounded-xl bg-gray-100 mb-6 overflow-hidden">
                        <img src="${p.img.replace('_200x200.jpg', '_480x480.jpg')}" alt="${cleanName}" class="w-full h-full object-contain group-hover:scale-110 transition duration-500">
                    </div>
                    <h3 class="font-bold text-lg mb-2">${cleanName}</h3>
                    <p class="text-gray-500 text-xs mb-4">${p.price} | ${p.moq}</p>
                    <div class="flex justify-between items-center text-xs font-bold">
                        <span class="text-blue-600">Factory Direct</span>
                        <a href="index.html#contact" class="px-3 py-1 bg-blue-100 text-blue-600 rounded-md hover:bg-blue-200 transition">Request Quote</a>
                    </div>
                </div>
    `;
}

const categories = {
    "Camping Tents": {
        filename: "camping-tents.html",
        title: "Wholesale Professional Camping Tents",
        header: "High-Performance Outdoor Shelters",
        sub: "From rapid-setup automatic tents to professional expedition gear. BSCI certified quality.",
        desc: "Direct from factory wholesale camping tents. Automatic quick-opening, professional waterproof ratings, and customized OEM service."
    },
    "Pop-up Tents": {
        filename: "pop-up-tents.html",
        title: "Wholesale Pop-up & Instant Setup Tents",
        header: "Instant Setup Pop-up Tents",
        sub: "Setup in seconds. Ideal for family camping, beach sun shades, and promotional outdoor events.",
        desc: "Direct from factory wholesale pop-up tents. 2-second setup, windproof folding mechanisms, and bulk export pricing."
    },
    "Changing Tents": {
        filename: "changing-tents.html",
        title: "Wholesale Portable Privacy Changing & Shower Tents",
        header: "Outdoor Privacy: Dressing & Shower Tents",
        sub: "Heavy-duty pop-up shelters for camping, beach bathing, and mobile toilets. 100% private.",
        desc: "Direct from factory wholesale changing tents. Automatic pop up dressing rooms, waterproof camping shower tents, and OEM bulk customization."
    },
    "Roof Top Tents": {
        filename: "roof-top-tents.html",
        title: "Wholesale Aluminum Hard Shell Roof Top Tents",
        header: "Overland Ready: Premium Rooftop Tents",
        sub: "Aerodynamic hard shell designs for 4x4 vehicles. 60-second setup for the ultimate off-road experience.",
        desc: "Direct from factory wholesale rooftop tents. Aluminum triangle clamshell designs, high waterproof ratings, and bulk supply for overland brands."
    },
    "Beach Tents": {
        filename: "beach-tents.html",
        title: "Wholesale Beach Tents & Sun Shelters",
        header: "Premium Sun Protection for Retail",
        sub: "Portable, high-SPF pop-up shelters for families and beachgoers. Lightweight and durable.",
        desc: "Direct from factory wholesale beach tents. Pop-up instant setup, UV protection fabric, and bulk supply for global importers."
    },
    "Outdoor Furniture": {
        filename: "outdoor-furniture.html",
        title: "Wholesale Outdoor Furniture & Equipment",
        header: "Durable Comfort for Every Campsite",
        sub: "Ergonomic chairs, aluminum tables, and premium camping cots. Built to last in the wild.",
        desc: "Direct from factory wholesale camping furniture. Lightweight folding chairs, aluminum tables, and OEM outdoor equipment."
    },
    "Inflatable Tents": {
        filename: "inflatable-tents.html",
        title: "Wholesale Inflatable Glamping Tents",
        header: "The Future of Glamping: Air-Beam Tech",
        sub: "Luxury inflatable houses and professional air shelters. 5-minute setup, 100% waterproof.",
        desc: "Direct from factory wholesale inflatable tents. Stay-Rigid air beam technology, luxury glamping designs, and full customization."
    }
};

for (const catName in categories) {
    const cat = categories[catName];
    const products = data[catName] || [];
    
    let html = getHead(cat.title, cat.desc);
    
    html += `
    <header class="bg-blue-900 text-white py-24 mt-20">
        <div class="max-w-7xl mx-auto px-4 text-center">
            <h1 class="text-5xl font-bold mb-6">${cat.header}</h1>
            <p class="text-xl text-blue-200 max-w-3xl mx-auto">${cat.sub}</p>
        </div>
    </header>

    <section class="py-24 bg-white">
        <div class="max-w-7xl mx-auto px-4">
            <h2 class="text-3xl font-bold mb-12 text-center text-blue-900 uppercase tracking-widest">Global Export Selection - 2026 ${catName}</h2>
            <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
                ${products.map((p, i) => generateProductCard(p, i)).join('')}
            </div>
        </div>
    </section>

    <section class="py-24 bg-gray-50 border-y">
        <div class="max-w-4xl mx-auto px-4 text-center">
            <h2 class="text-4xl font-bold mb-8 text-blue-900">Request a Bulk Quote</h2>
            <p class="text-xl text-gray-600 mb-10">Get factory-direct pricing and customization options for your brand.</p>
            <div class="flex flex-col md:flex-row justify-center gap-6">
                <a href="mailto:ray@xinqiu-tent.com" class="bg-blue-600 text-white px-10 py-5 rounded-xl font-bold hover:bg-blue-700 transition">Email Export Manager</a>
                <a href="https://wa.me/8618989341689" class="bg-green-600 text-white px-10 py-5 rounded-xl font-bold hover:bg-green-700 transition">WhatsApp Inquiry</a>
            </div>
        </div>
    </section>
    `;
    
    html += footer;
    html += "</body></html>";
    
    fs.writeFileSync(cat.filename, html);
    console.log("Generated " + cat.filename);
}
