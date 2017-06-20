# pDrive
pDrive enables you to instantly upload your learned models to your google drive

## Q & As
#### I'll get `googleapiclient.errors.HttpError`
Check your scope in google drive api. You can breifly check your settings by hitting
`curl "https://www.googleapis.com/oauth2/v3/tokeninfo?access_token={YOUR_ACCESS_TOKEN_HERE}"`
