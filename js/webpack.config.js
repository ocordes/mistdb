const path = require('path');

module.exports = {
	//mode: 'development',
        mode: 'production',
	entry: './src/index.js',
	output: {
	  filename: 'main.js',
          path: path.resolve(__dirname, '../src/app/static'),
        },
	module: {
	   rules: [
	     {
                test: /\.css$/,
                use: [
                  'style-loader',
                  'css-loader',
                ],
             },
           ],
       },
};
