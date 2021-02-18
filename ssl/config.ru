# frozen_string_literal: true

require 'rubygems'
require 'bundler'
Bundler.require(:default)

# Simple Sinatra app to complete challenge
class App < Sinatra::Base
  get "/.well-known/acme-challenge/#{ENV['ACME_CHALLENGE'].split('.').first}" do
    content_type :text
    ENV['ACME_CHALLENGE']
  end
end

run App
