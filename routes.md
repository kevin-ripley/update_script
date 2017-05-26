*

* Reset Password

*/

Route::post('password/token',
Route::post('password/reset',
Route::group*

* Users

*/

Route::get('users',
Route::post('users',
Route::get('users/{user}',
Route::patch('users/{user}',
Route::delete('users/{user}',
Route::get('users/{user}/history',
Route::post('users/{user}/archive',
Route::post('users/{user}/activate',
*

* User Media

*/

Route::get('user_media',
Route::get('/users/{user}/media',
*

* Profile Photos

*/

Route::get('users/{user}/profile_photos',
Route::post('users/{user}/profile_photos',
Route::delete('users/{user}/profile_photos/{profile_photo}',
Route::get('users/{user}/profile_photos/current',
Route::get('users/{user}/profile_photos/unset',
Route::patch('profile_photos/{profile_photo}',
Route::get('profile_photos/{profile_photo}',
Route::get('profile_photos/{profile_photo}/history',
Route::patch('profile_photos/{profile_photo}/approve',
Route::patch('profile_photos/{profile_photo}/disapprove',
*

* User Fields

*/

Route::get('user_fields',
Route::get('user_fields/{user_field}',
Route::post('user_fields',
Route::patch('user_fields/{user_field}',
Route::delete('user_fields/{user_field}',
Route::get('user_fields/{user_field}/history',
Route::get('user_fields/{user_field}/values',
*

* User Field Values

*/

Route::get('/user_field_values',
Route::get('/user_field_values/{user_field_value}',
Route::post('/user_field_values',
Route::patch('/user_field_values/{user_field_value}',
Route::delete('/user_field_values/{user_field_value}',
*

* Photos

*/

Route::get('photos',
Route::get('photos/{photo}',
Route::post('photos',
Route::patch('photos/{photo}',
Route::delete('photos/{photo}',
Route::get('photos/{photo}/history',
Route::patch('photos/{photo}/thumb',
Route::patch('photos/{photo}/approve',
Route::patch('photos/{photo}/disapprove',
Route::get('/users/{user}/photos',
Route::post('/users/{user}/photos',
Route::delete('/users/{user}/photos/{photo}',
*

* Videos

*/

Route::get('videos',
Route::get('videos/{video}',
Route::post('videos',
Route::patch('videos/{video}',
Route::delete('videos/{video}',
Route::get('videos/{video}/history',
Route::patch('videos/{video}/thumb',
Route::patch('videos/{video}/approve',
Route::patch('videos/{video}/disapprove',
Route::get('/users/{user}/videos',
Route::post('/users/{user}/videos',
Route::delete('/users/{user}/videos/{video}',
*

* Documents

*/

Route::get('documents',
Route::get('documents/{document}',
Route::post('documents',
Route::patch('documents/{document}',
Route::delete('documents/{document}',
Route::get('documents/{document}/history',
Route::patch('documents/{document}/approve',
Route::patch('documents/{document}/disapprove',
Route::get('/users/{user}/documents',
Route::post('/users/{user}/documents',
Route::delete('/users/{user}/documents/{document}',
*

* Links

*/

Route::get('links',
Route::get('links/{link}',
Route::post('links',
Route::patch('links/{link}',
Route::delete('links/{link}',
Route::get('links/{link}/history',
Route::patch('links/{link}/approve',
Route::patch('links/{link}/disapprove',
Route::get('/users/{user}/links',
Route::post('/users/{user}/links',
Route::delete('/users/{user}/links/{link}',
*

* Client Settings

*/

Route::get('client_settings/{client_id}',
Route::patch('client_settings/{client_id}/{key}',
Route::delete('client_settings/{client_id}/{key}',
*

* Available Media Types

*/

Route::get('media_types',
*

* Media Library

*/

Route::get('media_library',
*

* Modules

*/

Route::get('modules',
Route::get('modules/{module}',
Route::post('modules',
Route::patch('modules/{module}',
Route::delete('modules/{module}',
Route::get('modules/{module}/history',
Route::patch('modules/{module}/thumb',
Route::patch('modules/{module}/publish',
Route::patch('modules/{module}/unpublish',
Route::post('modules/{module}/duplicate',
*

* User Transcript

*/

Route::get('users/{user}/transcript',
Route::post('modules/{module}/completed_by/{user}',
Route::post('{media_type}/{media_id}/completed_by/{user}',
*

* Module Setting Presets

*/

Route::get('module_setting_presets',
Route::get('module_setting_presets/{preset}',
Route::post('module_setting_presets',
Route::patch('module_setting_presets/{preset}',
Route::delete('module_setting_presets/{preset}',
*

* Advocates

*/

Route::get('advocates',
Route::get('modules/{module}/advocates',
Route::post('modules/{module}/advocates/{advocate}',
Route::delete('modules/{module}/advocates/{advocate}',
*

* Rules

*/

Route::get('rules/{rule}',
Route::patch('rules/{rule}',
Route::post('rules',
Route::delete('rules/{rule}',
*

* Permissions

*/

Route::get('modules/{module}/permissions',
Route::post('modules/{module}/permissions',
Route::patch('modules/{module}/permissions/{rule}',
Route::delete('modules/{module}/permissions',
Route::post('modules/{module}/{media_type}/{media_id}/permissions',
Route::patch('modules/{module}/{media_type}/{media_id}/permissions/{rule}',
Route::delete('modules/{module}/{media_type}/{media_id}/permissions',
Route::post('users/{user}/media/{media}/permissions',
Route::patch('users/{user}/media/{media}/permissions/{rule}',
Route::delete('users/{user}/media/{media}/permissions}',
*

* Expressions

*/

Route::get('expressions',
*

* Tags

*/

Route::get('tags',
Route::post('tags',
Route::get('tags/{tag}',
Route::delete('tags/{tag}',
*

* Comments

*/

Route::get('users/{user}/comments',
Route::get('modules/{module}/comments',
Route::post('modules/{module}/comments',
Route::get('comments/{comment}',
Route::delete('comments/{comment}',
Route::patch('comments/{comment}',
Route::patch('comments/{comment}/flag',
Route::get('comments/{comment}/history',
*

* Likes

*/

Route::get('users/{user}/likes',
Route::get('modules/{module}/likes',
Route::post('modules/{module}/likes',
Route::delete('modules/{module}/likes',
Route::get('{media_type}/{media_id}/likes',
Route::post('{media_type}/{media_id}/likes',
Route::delete('{media_type}/{media_id}/likes',
Route::get('comments/{comment}/likes',
Route::post('comments/{comment}/likes',
Route::delete('comments/{comment}/likes',
*

* SCORM

*/

Route::get('scorm',
Route::post('scorm',
Route::get('scorm/{scorm}',
Route::patch('scorm/{scorm}',
Route::delete('scorm/{scorm}',
Route::get('scorm/{scorm}/data',
Route::post('scorm/{scorm}/data',
Route::get('scorm/{scorm}/history',
*

* AICC

*/

Route::get('aicc',
Route::post('aicc',
Route::get('aicc/{aicc}',
Route::patch('aicc/{aicc}',
Route::delete('aicc/{aicc}',
Route::get('aicc/{aicc}/data',
Route::post('aicc/{aicc}/data',
Route::get('aicc/{aicc}/history',
*

* Embedded Content

*/

Route::get('embedded_content',
Route::get('embedded_content/{embedded_content}',
Route::post('embedded_content',
Route::patch('embedded_content/{embedded_content}',
Route::delete('embedded_content/{embedded_content}',
Route::get('embedded_content/{embedded_content}/history',
