little info:
"Today we learn Application ko deploy kaise karenge inside a cloud Platform"
ab tak *projecct bana chuke hai *tested in lab *connected with MongoDb ?Remain Deployment on AWS Cloud
AWS have 'Code Pipeline'(help to connect with github) & 'Beanstack'(connect with 'codepiple' its help by providing environment(like:RAM,CPU,MEMORY,etc.))



In 'AWS' we use 2 service 'Code Pipeline' & 'Beanstack' its have many services

*****"Write the following in Terminal:"*****
#Clone Repositoryhttps://github.com/iNeuronai/review-scrapper-aws-main.git
git clone https://github.com/iNeuronai/review_sc_hindi.git
#go in folder 'review-scrapper-aws-main'
cd review-scrapper-aws-main
#go in file   #file visible, except .hiddenFile
ls
#To see hidden file
ls -a
#delete '.git' file
rm -rf .git
#now '.git' not show
ls -a

'Application.py' me sab data likha hai
#Do this changes in 'Application.py'
[line74] change MondoDb with your url
[lin12,17]'@cross_origin()' =means=> any contry(USA,France,...=Globally) can acces otherwise cloud don't allow
[line 88] ka changes are fine(host)


*****Push this code in your GitHub*****
Create repository in GitHub :'review_sc'
Write the following in Terminal:
git inti
git add .
git commit -m "first commit"
#Telling apna email,name dalo
git config --global user.email "brijrajbind12345@gmail.com"
git config --global user.name "Brijraj007"
git commit -m "first commit" #again commit
git branch -M main
git remote add origin https://github.com/Brijraj007/review_sc.git  #no Error bcz delete meta file
git push -u origin main
*****Done:Refresh your account*****


"""in "AWS" UnderStand to do Deploy init"""
*****'Github' me aagaya "pipline" me bhejenge
~del [BLUEPRINT : 'AWS' ke under 'Code Pipeline' fir iske under 'Beanstack'me Resource Banayenge aur connect karenge 'code pipeline' ke under]~
'Codepipeline' conect hota hai 'github' se (_CodeLega_) finally connect hota hai 'BeanStack' se (_CodeDega_)  =>Means 'CodePipeline' connect karta hai dono ko['github','BeanStack']

"BeanStack" took 3-5min to create environment jaha par deployment ho jayega