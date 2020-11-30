class App < Sinatra::Base
  get "/.well-known/acme-challenge/#{ENV['ACME_CHALLENGE'].split('.').first}" do
    content_type :text
    ENV['ACME_CHALLENGE']
  end
end
