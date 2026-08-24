def bom(name, fly_m2, floor_m2, pole_m, poles, inner_fab, mesh, zip_m, tape_m, stakes, labor):
    items = []
    items.append(('外帐 75D ripstop PU4000', fly_m2, 0.75, fly_m2 * 0.75))
    items.append(('地布 210D Oxford PU5000', floor_m2, 1.15, floor_m2 * 1.15))
    items.append(('内帐透气布', inner_fab, 0.62, inner_fab * 0.62))
    items.append(('内帐网纱', mesh, 0.48, mesh * 0.48))
    items.append(('玻纤杆 11mm', pole_m, 0.42, pole_m * 0.42))
    items.append(('杆套/接头/穿杆带', poles, 0.55, poles * 0.55))
    items.append(('钢地钉+营绳5mm', 1, stakes, stakes))
    items.append(('SBS拉链', zip_m, 0.55, zip_m * 0.55))
    items.append(('压胶带(全压胶)', tape_m, 0.075, tape_m * 0.075))
    items.append(('储物袋/挂钩/魔术贴/风绳扣', 1, 1.20, 1.20))
    items.append(('收纳袋(印logo)', 1, 1.45, 1.45))
    items.append(('吊牌+卡片 300g 黑印', 1, 0.35, 0.35))
    items.append(('说明书', 1, 0.18, 0.18))
    items.append(('纸箱(1顶1箱)', 1, 1.30, 1.30))
    items.append(('人工(裁剪/车缝/压胶/QC/包装)', 1, labor, labor))
    sub = sum(i[3] for i in items)
    loss = sub * 0.05
    total = sub + loss
    print('=' * 66)
    print(name)
    for n, q, p, a in items:
        print('  %-30s %7.1f x %5.2f = %6.2f' % (n, q, p, a))
    print('  %-30s %25.2f' % ('小计', sub))
    print('  %-30s %25.2f' % ('损耗 5%', loss))
    print('  >> 工厂总成本 USD %.2f' % total)
    for m, f in [(500, 1.00), (1000, 0.965), (3000, 0.93), (5000, 0.905)]:
        c = total * f
        print('     MOQ%5d: cost %5.2f | FOB@18%% %5.2f | @22%% %5.2f' % (m, c, c * 1.18, c * 1.22))
    return total


bom('TUNNEL 3  (420x240)', 31.2, 10.9, 15.5, 3, 11.5, 9.0, 13, 42, 3.40, 9.50)
bom('TUNNEL 5  (480x330)', 43.2, 17.1, 24.5, 4, 14.0, 12.5, 17, 56, 4.60, 13.00)
bom('TUNNEL 2x2 (500x230)', 36.3, 12.4, 21.2, 4, 16.5, 13.0, 20, 60, 4.20, 13.80)
