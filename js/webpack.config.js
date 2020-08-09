const path = require('path');

module.exports = {
	//mode: 'development',
        mode: 'production',
	//entry: './src/index.js',
        entry: './build/index.js',
        //devtool: 'source-map',
        devtool: false,
        performance: {
 	       hints: false,
               maxEntrypointSize: 512000,
               maxAssetSize: 512000
        },
	output: {
	  filename: 'main.js',
          path: path.resolve(__dirname, '../src/app/static/desk'),
        },
	module: {
	   rules: [
	     { test: /\.css$/, use: ['style-loader', 'css-loader' ] },
	     { test: /\.js$/, use: ["source-map-loader"], enforce: "pre" },
	     { test: /\.png$/, use: 'file-loader' }
           ],
       },
};
