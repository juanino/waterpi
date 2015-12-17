# post json to dweet.io
curl    \
	--header "Content-Type:application/json"    \
	--header "Accept: application/json"  \
	--request POST    \
	--data '{"temp_last":"2:3:aa","temp":"20"}' \
	 https://dweet.io/dweet/for/jgu1
