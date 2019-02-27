'use strict';

var gulp = require('gulp');
var uglify = require('gulp-uglify');
var concat = require('gulp-concat');
var sass = require('gulp-sass');
var uglifycss = require('gulp-uglifycss');
var spawn = require('child_process').spawn;

var lintPaths = [
	'gulpfile.js'
]

gulp.task('server:backend', function() {
	var devserverPosrt = process.env.PORT || 8000;
	process.env.PYTHONUNBUFFERED = 1;
	process.env.PYTHONDONTTWRITEBITECODE = 1;
	spawn('python3', ['manage.py', 'runserver', 'local.wlog.com:' + devserverPosrt], {
		stdio: 'inherit'
	});
});

gulp.task('sass', function(){
	gulp.src([
		'./staticDev/sass/*.sass'
		])
	.pipe(sass().on('error',sass.logError))
	.pipe(gulp.dest('./staticDev/css'));
});

gulp.task('css', function(){
	gulp.src([
		'./staticDev/css/*.css'
		])
	.pipe(concat('wlog.css'))
	.pipe(uglifycss({
		"maxLineLen": 80,
		"uglyComments": true
	}))
	.pipe(gulp.dest('./static/css'));
});

gulp.task('default', function() {
	gulp.start('server:backend');
	gulp.start('sass');
	gulp.start('css');
	gulp.watch(lintPaths);
});
