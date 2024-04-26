const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (input) => {
    console.log(input);  // ここで入力された内容を出力
    rl.close();  // 入力が終わったらリードラインインターフェースを閉じる
});

rl.on('close', () => {
    process.exit(0);  // プログラムを正常終了
});
