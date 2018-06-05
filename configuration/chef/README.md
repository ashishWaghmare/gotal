
This is simple example to develop on Centos in Test Driven Development way
We will use InSpec and Puppet default scripts to build simple reverse proxy

chef create cookbook reverse-proxy

Add to file : reverse-proxy\test\integration\default\default_test.rb

```ruby
describe package('nginx') do
  it { should be_installed }
end
```

Add to file :
```ruby
package 'nginx' do
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
describe service('nginx') do
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
Now add content but before we can test case
```ruby
describe command('curl localhost') do
  its('stdout') { should match('your text') }
end
```
Now lets create template to make dynamic page
```bash
chef generate template index.html
```
You can simply add below line in file index.html.erb
```ruby
This your text for index page
```
Now during deployment this template has to be place at right location
```ruby
template '/usr/share/nginx/html/index.html' do
  source 'index.html.erb'
  mode '0644'
end
```
Redploy and execute 
```bash
kitchen test
```

Credit: Mischa Taylor
