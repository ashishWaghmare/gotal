
This is simple example to develop on Centos in Test Driven Development way
We will use InSpec and Puppet default scripts to build simple reverse proxy

chef create cookbook reverse-proxy

Add to file : reverse-proxy\test\integration\default\default_test.rb

```ruby
describe package('ngnix') do
  it { should be_installed }
end
```

Add to file :
```ruby
package 'ngnix' do
  action :install
end
```
If this fails as your default installation will not have ngnix package

Add to file : reverse-proxy\reciepes\
```ruby
package 'epel' do
  action :install
end
```
Hopefully the test case is passed

Now service resource will be used 

Add to file: 
```ruby
describe service('ngnix') do
  it { should be_installed }
  it { should be_enabled }
  it { should be_running }
end
```
Now new test case should fail

Add to file: 
```ruby
service 'nginx' do
  action [ :enable, :start ]
end
```
Now add content 

chef generate template index.html

