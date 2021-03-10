function submitEntry() {
    editor.save().then((outputData) => {
        document.getElementById('journal-entry-input').value = JSON.stringify(outputData);
        document.getElementById('journal-entry-form').submit();
    });
}

function hideCurrJournalStats() {
    document.getElementById('journal-stats-tab').classList.remove('active');
    document.getElementById('journal-entry-tab').classList.add('active');
    for (item of document.getElementsByClassName('empty-for-chart-stats')) { item.style.display = 'block'; }
    if (currJournalStatsChart != undefined) { currJournalStatsChart.destroy(); }
    currJournalStatsctx.style.display = 'none';
}

let currSentimentScore;
let currJournalStatsChart;
const currJournalStatsctx = document.getElementById('curr-journal-stats-ctx');
for (i = 0; i < journalBlockReplacements.length; i++) { journalBlocks = journalBlocks.replaceAll(journalBlockReplacements[i][1], journalBlockReplacements[i][0]); }
journalBlocks = JSON.parse(journalBlocks);
let editor = new EditorJS({
    holder: 'journal-entry',
    tools: {
        header: {
            class: Header,
            shortcut: 'CMD+SHIFT+H',
            inlineToolbar: ['link'],
            config: {
                placeholder: 'Enter a header',
                levels: [2, 3],
                defaultLevel: 2
            }
        }
    },
    data: {blocks: journalBlocks.blocks}
});
let currJournalStatsChartJsData = {
    labels: ['Positive Sentiment', 'Negative Sentiment'],
    datasets: [{
        label: 'Sentimental Analysis',
        data: [],
        backgroundColor: ['rgba(69, 204, 88, 0.5)', 'rgba(220, 53, 69, 0.5)'],
        borderColor: ['rgba(69, 204, 88, 1)', 'rgba(220, 53, 69, 1)'],
        borderWidth: 1,
        fill: true
    }]
};
