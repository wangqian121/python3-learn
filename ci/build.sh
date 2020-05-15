!/bin/sh
function build(){
  mod_name=$1
  cmd=$2
  if [ -n $mod_name ] && [ -n $cmd ];then
    #避免写死JAVA_HOME
    sed -i '/JAVA_HOME/d' $mod_name/build.sh
    cd $mod_name && sh build.sh $cmd
    cd ..
  fi
}


#执行过程
if [ -d './target' ];then
  rm -rf ./target/*
else
  mkdir target
fi
