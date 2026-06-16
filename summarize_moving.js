const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, HeadingLevel, LevelFormat, AlignmentType } = require('docx');

const doc = new Document({
    numbering: {
        config: [
            {
                reference: 'bullet-list',
                levels: [{
                    level: 0,
                    format: LevelFormat.BULLET,
                    text: '•',
                    alignment: AlignmentType.LEFT,
                    style: { paragraph: { indent: { left: 720, hanging: 360 } } }
                }]
            }
        ]
    },
    sections: [{
        children: [
            new Paragraph({
                heading: HeadingLevel.TITLE,
                children: [new TextRun({ text: '搬厂注意事项和流程总结', bold: true, size: 48 })]
            }),
            new Paragraph({
                heading: HeadingLevel.HEADING_1,
                children: [new TextRun({ text: '一、 吉时与生肖避忌', bold: true })]
            }),
            new Paragraph({
                numbering: { reference: 'bullet-list', level: 0 },
                children: [
                    new TextRun('搬厂吉时：首选 '),
                    new TextRun({ text: '6月15日（庚申日）辰时（07:00-09:00）或已时（09:00-11:00）', color: 'FF0000', bold: true }),
                    new TextRun('。')
                ]
            }),
            new Paragraph({
                numbering: { reference: 'bullet-list', level: 0 },
                children: [
                    new TextRun({ text: '生肖避忌：属虎者（尤其是甲寅年出生）与当日日柱相冲，不宜主祭、率先跨门槛或点第一炷香', color: 'FF0000', bold: true }),
                    new TextRun('，可委托他人代办。')
                ]
            }),

            new Paragraph({
                heading: HeadingLevel.HEADING_1,
                children: [new TextRun({ text: '二、 佛菩萨像安置流程', bold: true })]
            }),
            new Paragraph({
                numbering: { reference: 'bullet-list', level: 0 },
                children: [
                    new TextRun({ text: '核心原则：先在旧厂告假 -> 用红布包好先搬 -> 新址吉时第一个安座 -> 洒净上香', color: 'FF0000', bold: true }),
                    new TextRun('。不可等杂物搬完才请菩萨。')
                ]
            }),
            new Paragraph({
                numbering: { reference: 'bullet-list', level: 0 },
                children: [
                    new TextRun('搬运细节：使用 '),
                    new TextRun({ text: '红布或黄布将像从头到脚包严', color: 'FF0000' }),
                    new TextRun('，香炉留少许旧灰红纸包好带走（香火不断），单独放车上，'),
                    new TextRun({ text: '严禁压重物或倒置', color: 'FF0000', bold: true }),
                    new TextRun('。')
                ]
            }),
            new Paragraph({
                numbering: { reference: 'bullet-list', level: 0 },
                children: [
                    new TextRun({ text: '入驻顺序：菩萨安座 -> 搬入财库（保险柜/账册）及首台生产设备（缠红布） -> 祭拜土地公', color: 'FF0000', bold: true }),
                    new TextRun('。')
                ]
            }),

            new Paragraph({
                heading: HeadingLevel.HEADING_1,
                children: [new TextRun({ text: '三、 祭拜仪式关键步骤', bold: true })]
            }),
            new Paragraph({
                numbering: { reference: 'bullet-list', level: 0 },
                children: [
                    new TextRun({ text: '开门旺气：负责人持红绸钥匙开门，口念“开门大吉、财源广进”，随后打全厂灯光、通风', color: 'FF0000' }),
                    new TextRun('。')
                ]
            }),
            new Paragraph({
                numbering: { reference: 'bullet-list', level: 0 },
                children: [
                    new TextRun('祭拜土地公：地点在工厂大门内侧，脸朝门外。备好三牲/斋菜、果品、发糕等。仪式约20分钟。')
                ]
            }),
            new Paragraph({
                numbering: { reference: 'bullet-list', level: 0 },
                children: [
                    new TextRun({ text: '仪式结束：全厂所有灯光和机器空转几分钟，象征“动起来、活起来”', color: 'FF0000', bold: true }),
                    new TextRun('。')
                ]
            }),

            new Paragraph({
                heading: HeadingLevel.HEADING_1,
                children: [new TextRun({ text: '四、 应急预案与禁忌', bold: true })]
            }),
            new Paragraph({
                numbering: { reference: 'bullet-list', level: 0 },
                children: [
                    new TextRun({ text: '突发停电：立即停止大型设备搬动', color: 'FF0000' }),
                    new TextRun('，改用临时照明确保上香，心态平稳。')
                ]
            }),
            new Paragraph({
                numbering: { reference: 'bullet-list', level: 0 },
                children: [
                    new TextRun({ text: '突降大雨：象征“财源滚滚”，仪式在室内照常进行', color: 'FF0000' }),
                    new TextRun('，注意红布遮挡避免雨水淋到佛像。')
                ]
            }),
            new Paragraph({
                numbering: { reference: 'bullet-list', level: 0 },
                children: [
                    new TextRun({ text: '重要禁忌：严禁使用倒头香（折断香）；严禁在供桌前说倒闭、亏钱等不吉利话', color: 'FF0000', bold: true }),
                    new TextRun('。')
                ]
            }),
            new Paragraph({
                numbering: { reference: 'bullet-list', level: 0 },
                children: [
                    new TextRun({ text: '特别提醒：6月15日金气旺，若遇金属器械断裂或巨响，预示“金声玉振、声名远播”，无需害怕', color: 'FF0000' }),
                    new TextRun('。')
                ]
            })
        ]
    }]
});

Packer.toBuffer(doc).then(buffer => {
    fs.writeFileSync('C:/Users/Ray/Desktop/搬厂注意事项和流程/搬厂注意事项和流程总结.docx', buffer);
    console.log('Document created successfully');
});
