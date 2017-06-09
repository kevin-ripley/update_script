Reset Password

post 'password/token'

post 'password/reset'

'middleware' => ['auth:api','reboot_user'

Users

get 'users'

post 'users'

get 'users/{user}'

patch 'users/{user}'

delete 'users/{user}'

get 'users/{user}/history'

post 'users/{user}/archive'

post 'users/{user}/activate'

User Profiles

post 'users/{user}/profile'

patch 'users/{user}/profile'

delete 'users/{user}/profile'

User Media

get 'user_media'

get '/users/{user}/media'

patch 'user_media/{media}/approve'

patch 'user_media/{media}/disapprove'

Profile Photos

get 'users/{user}/profile_photos'

post 'users/{user}/profile_photos'

delete 'users/{user}/profile_photos/{profile_photo}'

patch 'users/{user}/profile_photos/{profile_photo}/set_current'

patch 'users/{user}/profile_photos/unset_current'

patch 'profile_photos/{profile_photo}'

get 'profile_photos/{profile_photo}'

get 'profile_photos/{profile_photo}/history'

patch 'profile_photos/{profile_photo}/approve'

patch 'profile_photos/{profile_photo}/disapprove'

User Fields

get 'user_fields'

get 'user_fields/{type}/{field_id}'

post 'user_fields'

patch 'user_fields/{type}/{field_id}'

delete 'user_fields/{type}/{field_id}'

get 'user_fields/{type}/{field_id}/history'

get 'user_fields/{type}/{field_id}/values/'

get 'user_fields/{type}/{field_id}/values/{value_id}'

post 'user_fields/{type}/{field_id}/values/'

patch 'user_fields/{type}/{field_id}/values/{value_id}'

delete 'user_fields/{type}/{field_id}/values/{value_id}'

Photos

get 'photos'

get 'photos/{photo}'

post 'photos'

patch 'photos/{photo}'

delete 'photos/{photo}'

get 'photos/{photo}/history'

patch 'photos/{photo}/thumb'

patch 'photos/{photo}/approve'

patch 'photos/{photo}/disapprove'

get 'photos/{photo}/modules'

get '/users/{user}/photos'

post '/users/{user}/photos'

delete '/users/{user}/photos/{photo}'

Videos

get 'videos'

get 'videos/{video}'

post 'videos'

patch 'videos/{video}'

delete 'videos/{video}'

get 'videos/{video}/history'

patch 'videos/{video}/thumb'

patch 'videos/{video}/approve'

patch 'videos/{video}/disapprove'

get 'videos/{video}/history'

get '/users/{user}/videos'

post '/users/{user}/videos'

delete '/users/{user}/videos/{video}'

Documents

get 'documents'

get 'documents/{document}'

post 'documents'

patch 'documents/{document}'

delete 'documents/{document}'

get 'documents/{document}/history'

patch 'documents/{document}/approve'

patch 'documents/{document}/disapprove'

get 'documents/{document}/modules'

get '/users/{user}/documents'

post '/users/{user}/documents'

delete '/users/{user}/documents/{document}'

Links

get 'links'

get 'links/{link}'

post 'links'

patch 'links/{link}'

delete 'links/{link}'

get 'links/{link}/history'

patch 'links/{link}/approve'

patch 'links/{link}/disapprove'

get 'links/{link}/modules'

get '/users/{user}/links'

post '/users/{user}/links'

delete '/users/{user}/links/{link}'

Homework

get 'homework'

get 'homework/{homework}'

post 'homework'

patch 'homework/{homework}'

delete 'homework/{homework}'

get 'homework/{homework}/history'

Homework Responses

get 'homework/{homework}/responses/{response}'

post 'homework/{homework}/responses'

patch 'homework/{homework}/responses/{response}'

delete 'homework/{homework}/responses/{response}'

get 'homework/{homework}/responses/{response}/history'

patch 'homework/{homework}/responses/{response}/grade'

post 'homework/{homework}/responses/{response}/media'

delete 'homework/{homework}/responses/{response}/media'

Client Settings

get 'client_settings/{client_id}'

patch 'client_settings/{client_id}/{key}'

delete 'client_settings/{client_id}/{key}'

get 'client_settings/value/{key}'

Available Media

get 'media_types'

Media Library

get 'media_library'

Modules

get 'modules'

get 'modules/{module}'

post 'modules'

patch 'modules/{module}'

delete 'modules/{module}'

get 'modules/{module}/history'

patch 'modules/{module}/thumb'

patch 'modules/{module}/publish'

patch 'modules/{module}/unpublish'

post 'modules/{module}/duplicate'

User Transcript

get 'users/{user}/transcript'

post 'modules/{module}/completed_by/{user}'

post 'media/{media}/completed_by/{user}'

get 'users/{user}/incomplete_enrollments'

get 'users/{user}/enrollments/{enrollment}/transcript'

get 'users/{user}/transcript'

post 'modules/{module}/completed_by/{user}'

post '{media_type}/{media_id}/completed_by/{user}'

Module Setting

get 'module_setting_presets'

get 'module_setting_presets/{preset}'

post 'module_setting_presets'

patch 'module_setting_presets/{preset}'

delete 'module_setting_presets/{preset}'

Advocates

get 'advocates'

get 'modules/{module}/advocates'

post 'modules/{module}/advocates/{advocate}'

delete 'modules/{module}/advocates/{advocate}'

Rules

get 'rules/{rule}'

patch 'rules/{rule}'

post 'rules'

delete 'rules/{rule}'

Permissions

get 'modules/{module}/permissions'

post 'modules/{module}/permissions'

patch 'modules/{module}/permissions/{rule}'

delete 'modules/{module}/permissions'

post 'modules/{module}/{media_type}/{media_id}/permissions'

patch 'modules/{module}/{media_type}/{media_id}/permissions/{rule}'

delete 'modules/{module}/{media_type}/{media_id}/permissions'

post 'users/{user}/media/{media}/permissions'

patch 'users/{user}/media/{media}/permissions/{rule}'

delete 'users/{user}/media/{media}/permissions}'

Expressions

get 'expressions'

Enrollment

get 'enrollments'

get 'enrollments/{enrollment}'

post 'enrollments'

patch 'enrollments/{enrollment}'

patch 'enrollments/{enrollment}/activate'

patch 'enrollments/{enrollment}/deactivate'

post 'enrollments/{enrollment}/modules/{module}'

patch 'enrollments/{enrollment}/modules/{module}'

delete 'enrollments/{enrollment}/modules/{module}'

get 'enrollments/{enrollment}/log'

Tags

get 'tags'

post 'tags'

get 'tags/{tag}'

delete 'tags/{tag}'

Comments

get 'users/{user}/comments'

get 'modules/{module}/comments'

post 'modules/{module}/comments'

get 'discussions/{discussion}/comments'

post 'discussions/{discussion}/comments'

get 'homework/{homework}/responses/{response}/comments'

post 'homework/{homework}/responses/{response}/comments'

get 'comments/{comment}'

delete 'comments/{comment}'

patch 'comments/{comment}'

patch 'comments/{comment}/flag'

get 'comments/{comment}/history'

Likes

get 'users/{user}/likes'

get 'modules/{module}/likes'

post 'modules/{module}/likes'

delete 'modules/{module}/likes'

get '{media_type}/{media_id}/likes'

post '{media_type}/{media_id}/likes'

delete '{media_type}/{media_id}/likes'

get 'comments/{comment}/likes'

post 'comments/{comment}/likes'

delete 'comments/{comment}/likes'

SCORM

get 'scorm'

post 'scorm'

get 'scorm/{scorm}'

patch 'scorm/{scorm}'

delete 'scorm/{scorm}'

get 'scorm/{scorm}/data'

post 'scorm/{scorm}/data'

get 'scorm/{scorm}/history'

AICC

get 'aicc'

post 'aicc'

get 'aicc/{aicc}'

patch 'aicc/{aicc}'

delete 'aicc/{aicc}'

get 'aicc/{aicc}/data'

post 'aicc/{aicc}/data'

get 'aicc/{aicc}/history'

Embedded Content

get 'embedded_content'

get 'embedded_content/{embedded_content}'

post 'embedded_content'

patch 'embedded_content/{embedded_content}'

delete 'embedded_content/{embedded_content}'

get 'embedded_content/{embedded_content}/history'

Recognition Messages

get 'users/{user}/messages'

get 'users/{user}/messages/{message}'

post 'users/{user}/messages'

delete 'users/{user}/messages/{message}'

Discussions

get 'discussions'

post 'discussions'

get 'discussions/{discussion}'

patch 'discussions/{discussion}'

delete 'discussions/{discussion}'

get 'discussions/{discussion}/history'

