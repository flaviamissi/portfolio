from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix='/api')

about_data = {
    'experience': """I have over 6 years of experience as a software engineer, and have worked at both small startups and large organizations. While I'm a proficient full-stack developer, my expertise is in building scalable backend services (API services, stream processing, and async mechanisms).
""",
    'passions': """I love building things. While hard engineering problems are often intrinsically fun to tackle, I'm most attracted to solving real customer problems with a business justification. I'm looking for a senior individual contributor role where I can take on on collaborative team leadership responsibilites, and gain experience with architecture and project management.
""",
}

@api.route('/about')
def about():
    return jsonify(about_data)

projects_data = {
    'highlights': [
        'Migrated a monolithic Heroku Ruby on Rails API to multiple Scala services hosted on AWS. Delivered ahead of schedule, projected to save $18k/quarter.',
        'Presented research and proof-of-concept to convince team to move from Hadoop MR to Spark; reduced nodes by 60% and ran 5-8x faster.',
        'Automated test automation in ramp-up to large data center migration, saving hundreds of developer hours.',
        'Presented "Understanding the GIL to Prevent Race Conditions" at RubyConf 2016.',
        'Awarded patent for novel approach to item normalization in 3rd party catalog data feeds.',
    ],
    'recents': [
        'OpenGidget is an open-source fork of Raspbian Linux that makes it easier to auto-provision a headless Raspberry PI, get it onto your WiFi network, and deploy simple Python and Ruby scripts that run at startup - all without needing to plug in a keyboard/monitor.',
        'My Medium blog covers my ongoing attempts to instrument and automate everything in my house.',
    ],
    'other': [
        'Volunteer at Boys and Girls club (since 2008)',
        'Active member of The Seattle Ruby on Rails Developers Meetup Group.',
    ]
}

@api.route('/projects')
def projects():
    return jsonify(projects_data)

interests_data = [
    {
        'title': 'Deep learning',
        'description': 'It\'s an exciting time for machine learning. I\'m working through several online classes, and swap articles with collegues.',
    },
    {
        'title': 'RC Planes and Boats',
        'description': 'I\'ve been an enthusiastic hobbiest since I was a teenager - but only as an adult am I able to afford the higher-quality devices. I like to modify existing kits to improve speed, and add instrumentation.',
    },
    {
        'title': 'Mountaineering',
        'description': 'I live in the Pacific Northwest, home of some of the greatest mountains and trails in the country. I enjoy spending weekends on scrambles and getting lost in the woods.',
    }
]

@api.route('/interests')
def interests():
    return jsonify(interests_data)
