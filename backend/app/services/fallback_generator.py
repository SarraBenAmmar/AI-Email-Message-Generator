"""
Fallback generator for when AI services are unavailable
"""
from typing import List
from models.schemas import SequenceItem, GenerationRequest, Channel, Tone, Audience

# Comprehensive templates for different channels
CHANNEL_TEMPLATES = {
    Channel.EMAIL: {
        Tone.PROFESSIONAL: {
            Audience.PROSPECT: {
                "intro": "Subject: Following up on our conversation about {topic}\n\nDear [Contact Name],\n\nI hope this message finds you well. I wanted to follow up regarding our recent discussion about {topic}. Based on your goals, I believe we can provide significant value to your organization.\n\nWould you be available for a brief call next week to explore this further?\n\nBest regards,\n[Your Name]",
                "follow_up": "Subject: Checking in about {topic}\n\nHi [Contact Name],\n\nI wanted to follow up on my previous message about {topic}. I understand you're busy, but I didn't want this to get lost in your inbox.\n\nAre you available for a quick 15-minute call to discuss how we can help achieve your goals?\n\nLooking forward to your response.\n\nBest,\n[Your Name]",
                "closing": "Subject: Final follow-up regarding {topic}\n\nHello [Contact Name],\n\nThis will be my final attempt to connect regarding {topic}. If the timing isn't right or you've found another solution, I completely understand.\n\nShould your needs change in the future, please don't hesitate to reach out. I'd be happy to help.\n\nWishing you the best in your endeavors.\n\nSincerely,\n[Your Name]"
            },
            Audience.CLIENT: {
                "intro": "Subject: Checking in on your experience with {topic}\n\nDear [Client Name],\n\nI hope you're finding value in our service and everything is meeting your expectations regarding {topic}. We're committed to ensuring your success with our solution.\n\nIs there anything we can do to improve your experience or help you achieve better results?\n\nBest regards,\n[Your Name]",
                "follow_up": "Subject: How can we help with {topic}?\n\nHi [Client Name],\n\nI wanted to check if there's anything we can assist you with to maximize your results from {topic}.\n\nWe have some new features/resources that might be valuable for your use case. Would you be interested in a quick walkthrough?\n\nBest,\n[Your Name]",
                "closing": "Subject: Thank you for your partnership on {topic}\n\nHello [Client Name],\n\nI wanted to personally thank you for your business and partnership regarding {topic}. We truly appreciate having you as a client.\n\nIf there's ever anything we can do to better support you, please don't hesitate to reach out.\n\nSincerely,\n[Your Name]"
            }
        },
        Tone.FRIENDLY: {
            Audience.PROSPECT: {
                "intro": "Subject: Great connecting with you about {topic}!\n\nHi [Contact Name],\n\nIt was great learning about your work! I was particularly interested in what you're doing with {topic}.\n\nI'd love to explore how we might work together to help with your goals. Are you free for a quick chat next week?\n\nCheers,\n[Your Name]",
                "follow_up": "Subject: Following up\n\nHey [Contact Name],\n\nJust circling back on {topic} - would love to hear your thoughts when you have a moment!\n\nNo pressure at all, just didn't want this to slip through the cracks.\n\nBest,\n[Your Name]",
                "closing": "Subject: Last try on {topic}\n\nHi [Contact Name],\n\nI know you're busy, so I'll leave the ball in your court regarding {topic}. Feel free to reach out if you'd ever like to connect!\n\nWishing you all the best,\n[Your Name]"
            }
        }
    },
    
    Channel.BLOG_POST: {
        Tone.PROFESSIONAL: {
            Audience.PROSPECT: {
                "intro": "# The Complete Guide to {topic}\n\nIn today's fast-paced business environment, understanding {topic} has become essential for success. This comprehensive guide will walk you through everything you need to know.",
                "follow_up": "## Key Strategies for Mastering {topic}\n\nAfter extensive research and client work, we've identified these proven approaches to {topic} that deliver consistent results.",
                "closing": "## Conclusion: Your Path Forward with {topic}\n\nAs we've explored, effective implementation of {topic} can transform your business outcomes. The key is to start small, measure results, and iterate consistently."
            }
        },
        Tone.STORYTELLING: {
            Audience.PROSPECT: {
                "intro": "# The Journey of Discovering {topic}\n\nLet me take you back to when I first encountered the challenges of {topic}. It was a humid Tuesday afternoon when everything changed...",
                "follow_up": "## The Turning Point in {topic}\n\nJust when I thought we'd exhausted all options for {topic}, a chance conversation revealed a completely different approach that transformed our results.",
                "closing": "## What {topic} Taught Me About Business\n\nLooking back on our journey with {topic}, the most valuable lesson wasn't about the technical details, but about perseverance and innovation."
            }
        }
    },
    
    Channel.SOCIAL_MEDIA: {
        Tone.PROFESSIONAL: {
            Audience.PROSPECT: {
                "intro": "🚀 Excited to share insights about {topic}! \n\nThis is changing how we approach business challenges. What's your experience been?\n\n#BusinessTips #Growth",
                "follow_up": "💡 Quick tip about {topic}: \n\nStart with the fundamentals and build from there. Consistency is key to seeing real results!\n\n#ProfessionalAdvice #Success",
                "closing": "🎯 Final thought on {topic}: \n\nThe most successful implementations focus on sustainable practices rather than quick fixes.\n\nWhat strategies have worked for you? #Business #Strategy"
            }
        },
        Tone.FRIENDLY: {
            Audience.PROSPECT: {
                "intro": "Hey everyone! 👋 Been thinking a lot about {topic} lately...\n\nWhat are your thoughts on this? Would love to hear from this amazing community! 💬",
                "follow_up": "Quick update on {topic} - some really interesting conversations happening!\n\nKeep the ideas coming, you folks are awesome! 🙌",
                "closing": "Last post in this {topic} series! Thanks for all the amazing responses.\n\nYou've given me so much to think about! 🤗 #CommunityLove"
            }
        }
    },
    
    Channel.PRODUCT_DESCRIPTION: {
        Tone.PROFESSIONAL: {
            Audience.PROSPECT: {
                "intro": "Introducing Our {topic} Solution\n\nDesigned specifically to address the challenges professionals face with {topic}. Streamline your workflow and achieve better results.",
                "follow_up": "Key Features That Set Us Apart:\n• Intelligent automation for {topic}\n• User-friendly dashboard\n• Comprehensive analytics suite\n• 24/7 dedicated support",
                "closing": "Why Choose Our {topic} Platform?\n\nJoin thousands of satisfied users who have transformed their approach to {topic}. Experience the difference today."
            }
        },
        Tone.FRIENDLY: {
            Audience.PROSPECT: {
                "intro": "Meet Your New {topic} Best Friend! 🤝\n\nWe've created something special to make {topic} easier and more effective than ever before.",
                "follow_up": "What Makes Our {topic} Tool Awesome:\n✨ Makes complex tasks simple\n✨ Grows with your needs\n✨ Always has your back",
                "closing": "Ready to Fall in Love with {topic}?\n\nSee why our users can't stop talking about how we've transformed their {topic} experience! 💫"
            }
        }
    },
    
    Channel.SCRIPT: {
        Tone.PROFESSIONAL: {
            Audience.PROSPECT: {
                "intro": "[Opening]\nHi everyone, today I want to discuss {topic} and why it's become such a critical factor in today's business landscape.\n\n[Main Points]\nFirst, let's understand the core challenges around {topic}. Many organizations struggle with implementation and consistency...\n\n[Transition]\nNow that we've identified the challenges, let's explore some practical solutions.",
                "follow_up": "[Recap]\nIn our previous discussion, we covered the fundamental challenges of {topic}. Today, we'll dive into actionable strategies.\n\n[Key Strategies]\nStrategy 1: Start with a clear assessment of your current situation regarding {topic}...\nStrategy 2: Develop a phased implementation plan...\nStrategy 3: Establish clear metrics for success...\n\n[Question]\nWhich of these strategies resonates most with your experience?",
                "closing": "[Summary]\nAs we wrap up our discussion on {topic}, let's recap the key takeaways...\n\n[Final Thought]\nRemember, success with {topic} comes from consistent effort and continuous improvement.\n\n[Call to Action]\nIf you found this valuable, I'd love to hear about your experiences in the comments below."
            }
        },
        Tone.STORYTELLING: {
            Audience.PROSPECT: {
                "intro": "[Setting the Scene]\nI want to take you back to a time when I first encountered the real challenges of {topic}. It was during a project that completely changed my perspective...\n\n[The Challenge]\nWe were facing what seemed like an impossible situation with {topic}. The team was frustrated, and progress had stalled...\n\n[The Turning Point]\nThen we discovered a different approach to {topic} that changed everything.",
                "follow_up": "[Continuing the Journey]\nLast time, I shared how we hit a wall with {topic}. Today, I want to tell you about the breakthrough that transformed our results...\n\n[The Solution]\nIt wasn't about working harder on {topic}, but working smarter. We realized that the key was...\n\n[The Impact]\nThe results were incredible. Within weeks, we saw dramatic improvements in our approach to {topic}.",
                "closing": "[The Resolution]\nLooking back on our journey with {topic}, I'm struck by how much we learned through the process...\n\n[The Moral]\nThe biggest lesson? That challenges with {topic} are often opportunities in disguise.\n\n[Final Reflection]\nI hope our story inspires you to approach {topic} with fresh eyes and renewed energy."
            }
        }
    },
    
    Channel.NEWSLETTER: {
        Tone.PROFESSIONAL: {
            Audience.PROSPECT: {
                "intro": "📬 Welcome to Our {topic} Newsletter!\n\nIn this edition, we're exploring the latest trends and strategies in {topic}. We've curated the most valuable insights to help you stay ahead.",
                "follow_up": "🔍 Deep Dive: Understanding {topic}\n\nLet's explore the key components that make {topic} so impactful for modern businesses. From foundational principles to advanced techniques.",
                "closing": "🎯 Next Steps with {topic}\n\nReady to take action? Here are practical steps you can implement immediately to improve your results with {topic}."
            }
        },
        Tone.FRIENDLY: {
            Audience.PROSPECT: {
                "intro": "Hey there! 👋\n\nWelcome to our {topic} newsletter - your monthly dose of insights and inspiration! We're excited to share what we've been learning about {topic}.",
                "follow_up": "The Cool Stuff We Found About {topic} 🤓\n\nWe've been digging into {topic} and found some really interesting patterns and strategies you should know about!",
                "closing": "Your {topic} Action Plan 🚀\n\nHere are some simple but powerful ways you can start applying these {topic} insights right away. You've got this!"
            }
        }
    },
    
    Channel.CONTENT_IDEAS: {
        Tone.PROFESSIONAL: {
            Audience.PROSPECT: {
                "intro": "📋 Content Strategy Ideas for {topic}\n\n1. 'The Complete Beginner's Guide to {topic}'\n2. '5 Common Mistakes to Avoid in {topic}'\n3. 'How to Measure ROI in {topic} Initiatives'",
                "follow_up": "🎯 Advanced {topic} Content Concepts\n\n4. 'Case Study: Successful {topic} Implementation at Scale'\n5. 'The Future of {topic}: Emerging Trends and Technologies'\n6. 'Expert Panel: Diverse Perspectives on {topic}'",
                "closing": "💡 Innovative {topic} Content Formats\n\n7. 'Interactive Workshop: Hands-on {topic} Training'\n8. 'Data-Driven Insights: What the Numbers Say About {topic}'\n9. 'Creating Your Personalized {topic} Roadmap'"
            }
        },
        Tone.FRIENDLY: {
            Audience.PROSPECT: {
                "intro": "💡 Fun Content Ideas About {topic}!\n\n1. '{topic} Made Simple: A No-Jargon Guide'\n2. 'The Top 3 Things Everyone Gets Wrong About {topic}'\n3. 'How I Finally Figured Out {topic} (And You Can Too!)'",
                "follow_up": "🚀 More Awesome {topic} Topics\n\n4. 'Real Stories: How {topic} Changed Our Business'\n5. 'The Coolest Tools for Mastering {topic}'\n6. '{topic} Q&A: Your Questions Answered'",
                "closing": "🎉 Creative Ways to Talk About {topic}\n\n7. 'The {topic} Challenge: 7 Days to Better Results'\n8. 'Behind the Scenes: Our {topic} Journey'\n9. 'Community Spotlight: Amazing {topic} Success Stories'"
            }
        }
    }
}

class FallbackGenerator:
    def __init__(self):
        self.templates = CHANNEL_TEMPLATES
        print("✅ Fallback generator initialized for multiple channels")
    
    async def generate_sequence(self, request: GenerationRequest) -> List[SequenceItem]:
        """Generate sequence using templates for any channel"""
        print(f"🎯 Fallback: Generating {request.sequence_length} {request.channel.value} items")
        
        sequence = []
        
        # Get appropriate template
        channel_templates = self.templates.get(
            request.channel, 
            self.templates[Channel.EMAIL]  # Default fallback
        )
        tone_templates = channel_templates.get(
            request.tone,
            list(channel_templates.values())[0]  # First available tone
        )
        audience_templates = tone_templates.get(
            request.audience,
            list(tone_templates.values())[0]  # First available audience
        )
        
        # Define purposes based on sequence length
        purposes = ["Introduction", "Follow-up", "Value Proposition", "Call to Action", "Closing"]
        
        for i in range(request.sequence_length):
            purpose = purposes[i] if i < len(purposes) else f"Message {i+1}"
            
            # Get template content based on step
            if i == 0:
                content = audience_templates.get("intro", list(audience_templates.values())[0])
            elif i == request.sequence_length - 1:
                content = audience_templates.get("closing", list(audience_templates.values())[-1])
            else:
                content = audience_templates.get("follow_up", list(audience_templates.values())[1])
            
            # Customize content based on prompt
            customized_content = content.replace("{topic}", request.prompt)
            
            # Extract subject and body based on channel type
            if request.channel == Channel.EMAIL and "Subject:" in customized_content:
                parts = customized_content.split("Subject:", 1)[1]
                lines = parts.strip().split("\n", 1)
                subject = lines[0].strip()
                body = lines[1].strip() if len(lines) > 1 else ""
            else:
                # For non-email channels, generate appropriate subject
                subject = f"{purpose}: {request.prompt}"
                body = customized_content
            
            sequence.append(SequenceItem(
                subject=subject,
                body=body,
                step=i + 1,
                purpose=purpose
            ))
        
        return sequence