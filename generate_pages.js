const fs = require('fs');

const data = JSON.parse(fs.readFileSync('scraped_products_full.json', 'utf8'));

const nav = `
                <div class="hidden md:flex space-x-6 text-xs font-semibold uppercase tracking-wider items-center">
                    <a href="index.html" class="hover:text-blue-600 transition">Home</a>
                    <a href="camping-tents.html" class="hover:text-blue-600 transition">Camping</a>
                    <a href="pop-up-tents.html" class="hover:text-blue-600 transition">Pop-up</a>
                    <a href="changing-tents.html" class="hover:text-blue-600 transition">Changing</a>
                    <a href="index.html#faq" class="hover:text-blue-600 transition">Sourcing FAQ</a>
                    <a href="index.html#about" class="hover:text-blue-600 transition">Factory</a>
                    <a href="index.html#news" class="hover:text-blue-600 transition">Intelligence</a>
                    <a href="index.html#contact" class="px-5 py-2 bg-blue-600 text-white rounded-full hover:bg-blue-700 transition">Inquiry</a>
                </div>
`;

const footer = `
    <footer class="bg-gray-900 text-white py-20 border-t border-slate-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid md:grid-cols-3 gap-16">
            <div>
                <span class="text-3xl font-bold">XINQIU TENT</span>
                <p class="mt-6 opacity-60 text-sm leading-relaxed mb-6">Ningbo Xinqiu Travelling Products Co., Ltd. - Your trusted B2B partner in the wild since 2006.</p>
                <div class="flex space-x-4 text-xl text-slate-400">
                    <a href="https://www.linkedin.com/company/ningbo-xinqiu-travelling-products-co-ltd/" target="_blank" class="hover:text-blue-500 transition" title="LinkedIn Company Page"><i class="fab fa-linkedin"></i></a>
                    <a href="https://www.linkedin.com/in/shichen-cheng" target="_blank" class="hover:text-blue-400 transition" title="LinkedIn Personal Profile"><i class="far fa-id-card"></i></a>
                    <a href="https://www.instagram.com/windvalleyoutdoor/" target="_blank" class="hover:text-pink-500 transition" title="Instagram Business Page"><i class="fab fa-instagram"></i></a>
                    <a href="https://www.instagram.com/crsacy?igsh=MWF4eWpsZjduZXJ3dw%3D%3D&utm_source=qr" target="_blank" class="hover:text-pink-400 transition" title="Instagram Personal Profile"><i class="far fa-user-circle"></i></a>
                    <a href="https://www.tiktok.com/@windvalleyoutdoor?_r=1&_t=ZT-974T2xMVl1B" target="_blank" class="hover:text-slate-100 transition" title="TikTok Page"><i class="fab fa-tiktok"></i></a>
                    <a href="https://www.facebook.com/share/18nmvYHjVt/?mibextid=wwXIfr" target="_blank" class="hover:text-blue-600 transition" title="Facebook Page"><i class="fab fa-facebook"></i></a>
                </div>
            </div>
            <div>
                <h5 class="text-lg font-bold mb-6">B2B Quick Links</h5>
                <ul class="space-y-4 text-sm opacity-60">
                    <li><a href="camping-tents.html" class="hover:text-blue-400">Wholesale Camping Tents</a></li>
                    <li><a href="pop-up-tents.html" class="hover:text-blue-400">Pop-up Instant Tents</a></li>
                    <li><a href="changing-tents.html" class="hover:text-blue-400">Privacy Changing Rooms</a></li>
                    <li><a href="index.html#faq" class="hover:text-blue-400">Technical FAQ</a></li>
                </ul>
            </div>
            <div>
                <h5 class="text-lg font-bold mb-6">Ningbo Factory</h5>
                <p class="opacity-60 text-sm leading-relaxed">No. 208, Longjiaoshan Rd., Beilun Dist., <br>Ningbo, Zhejiang, China 315806</p>
                <p class="mt-4 opacity-60 text-sm">Email: ray@xinqiu-tent.com</p>
            </div>
        </div>
        <div class="max-w-7xl mx-auto px-4 text-center mt-20 pt-8 border-t border-gray-800 opacity-40 text-xs">
            &copy; 2026 Ningbo Xinqiu Travelling Products Co., Ltd. All rights reserved.
        </div>
    </footer>
    <!-- WhatsApp Floating Button -->
    <a href="https://wa.me/8618989341689" target="_blank" class="fixed bottom-8 right-8 z-[100] bg-green-500 text-white p-4 rounded-full shadow-2xl hover:bg-green-600 transition-all group flex items-center space-x-2">
        <i class="fab fa-whatsapp text-2xl"></i>
        <span class="max-w-0 overflow-hidden group-hover:max-w-xs transition-all duration-500 ease-in-out whitespace-nowrap font-bold">Chat with Factory Manager</span>
    </a>
`;

const trustBar = `
    <!-- Data Trust Bar (Nastocamp Style) -->
    <section class="py-12 bg-slate-900 text-white border-y border-slate-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
                <div>
                    <div class="text-3xl font-black text-blue-500">2006</div>
                    <div class="text-[10px] uppercase tracking-[0.2em] opacity-50 mt-2">Established Since</div>
                </div>
                <div>
                    <div class="text-3xl font-black text-blue-500">BSCI</div>
                    <div class="text-[10px] uppercase tracking-[0.2em] opacity-50 mt-2">Certified Factory</div>
                </div>
                <div>
                    <div class="text-3xl font-black text-blue-500">5,500㎡</div>
                    <div class="text-[10px] uppercase tracking-[0.2em] opacity-50 mt-2">Production Facility</div>
                </div>
                <div>
                    <div class="text-3xl font-black text-blue-500">80+</div>
                    <div class="text-[10px] uppercase tracking-[0.2em] opacity-50 mt-2">Countries Served</div>
                </div>
            </div>
        </div>
    </section>
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
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&display=swap');
        body { font-family: 'Inter', sans-serif; scroll-behavior: smooth; }
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
                <!-- B2B Expert Style -->
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
                            <p class="text-slate-500 text-[10px] italic mb-8">* Full OEM/ODM customization available. Contact for CAD preview.</p>
                        </div>
                        
                        <a href="index.html#contact" class="w-full py-4 rounded-xl border-2 border-blue-500/30 text-blue-400 font-black text-xs uppercase tracking-widest flex items-center justify-center gap-3 hover:bg-blue-600 hover:text-white hover:border-blue-600 transition-all duration-300">
                            Get A Bulk Quote <i class="fas fa-arrow-right text-[10px]"></i>
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

const faqs = [
    { q: "How many years of manufacturing experience do you have?", a: "We have over 20 years of expertise since 2006. Our 5,500㎡ facility specializes in high-durability family and professional camping gear." },
    { q: "Is your factory BSCI or ISO certified?", a: "Yes, we are a BSCI-certified factory. We strictly adhere to international labor and quality standards, making us a reliable partner for EU and North American brands." },
    { q: "What is your Minimum Order Quantity (MOQ)?", a: "Our MOQ varies by style to accommodate different market needs. We strongly support new partners by offering small-batch trial orders for first-time cooperation to lower your risk." },
    { q: "What fabrics and waterproof ratings do you provide?", a: "We offer Oxford, Polyester, and Cotton with PA, PU, or Silicone coatings (300mm - 30,000mm). All seams are heat-taped and windows use waterproof plackets. To ensure your absolute confidence, we provide FREE fabric samples for your pre-production waterproof tests. Mass production only proceeds after your testing is successfully passed." },
    { q: "Do your tents provide professional UV protection?", a: "Yes, we achieve UPF 50+ using Silver, Vinyl, or Titanium Silver coatings (meeting US ASTM D6603 & EU EN 13758). We offer free fabric swatches for your pre-order UV testing to verify compliance before we initiate mass manufacturing." },
    { q: "What is your logistical advantage?", a: "Logistical efficiency is our pride. Our factory is strategically located near Beilun Port (Ningbo); our containers can reach the pier in just 30 minutes, ensuring rapid loading and significantly reducing total transit time." },
    { q: "What are your internal QC procedures?", a: "We maintain a 0-defect goal. In addition to material audits, we conduct 100% full inspection after assembly for every single unit before packing to ensure structural and aesthetic integrity." }
];

function generateFAQSection() {
    return `
    <section id="faq" class="py-24 bg-gray-50 border-t">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-4xl font-bold text-center text-blue-900 mb-16 uppercase tracking-widest">B2B Sourcing Technical FAQ</h2>
            <div class="space-y-4">
                ${faqs.map((f, i) => `
                <div class="bg-white rounded-2xl border border-gray-200 overflow-hidden">
                    <button class="w-full px-8 py-6 text-left flex justify-between items-center hover:bg-gray-50 transition" onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('i').classList.toggle('rotate-180')">
                        <span class="font-bold text-lg text-blue-900">${i + 1}. ${f.q}</span>
                        <i class="fas fa-chevron-down text-blue-600 transition-transform"></i>
                    </button>
                    <div class="px-8 pb-8 text-gray-600 leading-relaxed hidden">
                        ${f.a}
                    </div>
                </div>
                `).join('')}
            </div>
        </div>
    </section>
    `;
}

const categories = {
    "Camping Tents": {
        filename: "camping-tents.html",
        title: "Wholesale Camping Tent Factory - Professional OEM/ODM Manufacturing",
        header: "High-Performance Outdoor Shelters",
        sub: "From rapid-setup automatic tents to professional expedition gear. BSCI certified quality.",
        desc: "Trusted China camping tent factory since 2006. Specializing in high-durability family tents, automatic pole structures, and custom OEM manufacturing for global outdoor brands."
    },
    "Pop-up Tents": {
        filename: "pop-up-tents.html",
        title: "Wholesale Pop-up Tents Supplier - Instant Setup Solutions",
        header: "Instant Setup Pop-up Tents",
        sub: "Setup in seconds. Ideal for family camping, beach sun shades, and promotional outdoor events.",
        desc: "Professional pop-up tent manufacturer. Offering bulk supply for quick-open beach tents, instant sun shelters, and lightweight camping tents with custom branding."
    },
    "Changing Tents": {
        filename: "changing-tents.html",
        title: "Portable Privacy Tents & Shower Shelters - Bulk Factory Supply",
        header: "Outdoor Privacy: Dressing & Shower Tents",
        sub: "Heavy-duty pop-up shelters for camping, beach bathing, and mobile toilets. 100% private.",
        desc: "Leading manufacturer of portable privacy tents. Heavy-duty 210D Oxford dressing rooms and mobile shower shelters. Verified quality for bulk B2B importers."
    },
    "Roof Top Tents": {
        filename: "roof-top-tents.html",
        title: "Aluminum Hard Shell Roof Top Tents - China Sourcing Agent",
        header: "Overland Ready: Premium Rooftop Tents",
        sub: "Aerodynamic hard shell designs for 4x4 vehicles. 60-second setup for the ultimate off-road experience.",
        desc: "B2B supplier of premium aluminum rooftop tents. Clamshell triangle designs, 3000mm+ waterproof index, and bulk manufacturing for overland brands."
    },
    "Beach Tents": {
        filename: "beach-tents.html",
        title: "Bulk Beach Tents & Sun Shelters - UV Protection Factory",
        header: "Premium Sun Protection for Retail",
        sub: "Portable, high-SPF pop-up shelters for families and beachgoers. Lightweight and durable.",
        desc: "OEM factory for UPF 50+ beach tents and cabanas. Lightweight portable sun shelters and family beach umbrellas for global retailers and wholesalers."
    },
    "Outdoor Furniture": {
        filename: "outdoor-furniture.html",
        title: "Wholesale Outdoor Furniture & Camping Equipment",
        header: "Durable Comfort for Every Campsite",
        sub: "Ergonomic chairs, aluminum tables, and premium camping cots. Built to last in the wild.",
        desc: "China manufacturer of folding camping furniture. High-capacity aluminum chairs, roll-top tables, and lightweight outdoor gear for professional campers."
    },
    "Inflatable Tents": {
        filename: "inflatable-tents.html",
        title: "Wholesale Inflatable Glamping Tents - Air-Beam Technology",
        header: "The Future of Glamping: Air-Beam Tech",
        sub: "Luxury inflatable houses and professional air shelters. 5-minute setup, 100% waterproof.",
        desc: "Pioneering manufacturer of Stay-Rigid air-beam tents. Luxury glamping domes and inflatable family tents for eco-resorts and premium rental businesses."
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

    ${catName === "Camping Tents" ? trustBar : ""}

    <section class="py-24 bg-white">
        <div class="max-w-7xl mx-auto px-4">
            <h2 class="text-3xl font-bold mb-12 text-center text-blue-900 uppercase tracking-widest">Global Export Selection - 2026 ${catName}</h2>
            <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
                ${products.map((p, i) => generateProductCard(p, i)).join('')}
            </div>
        </div>
    </section>

    ${generateFAQSection()}

    <section class="py-24 bg-white border-y">
        <div class="max-w-4xl mx-auto px-4 text-center">
            <h2 class="text-4xl font-bold mb-8 text-blue-900">Request a Bulk Quote</h2>
            <p class="text-xl text-gray-600 mb-10">Get factory-direct pricing and technical specs for your brand.</p>
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
